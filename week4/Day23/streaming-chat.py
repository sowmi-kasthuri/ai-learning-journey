from dotenv import load_dotenv
import os
import requests
import logging
import time
import json

# 1️⃣ load env
load_dotenv()
#print("DEBUG URL:", os.getenv("OPENROUTER_API_URL"))

url = os.getenv("OPENROUTER_API_URL")
key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("MODEL")


# 2️⃣ set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("streaming.log"), logging.StreamHandler()]
)


# 3️⃣ ask question
question = input("You : ")



# 4️⃣ build json payload
payload = {
    "model":model,
    "messages":[
       # {"role":"system", "content":"Answer in one or two sentences"},
        {"role":"user", "content":question }
        ],
    "stream":True
}


# 5️⃣ set headers - Bearer auth
headers = {
    "Authorization":f"Bearer {key}",
    "Content-Type":"application/json"
}


# 6️⃣Send request with stream=True
try:
    response = requests.post(url, headers=headers, json=payload, stream=True)
    response.raise_for_status() # catches 4xx/5xx
except requests.exceptions.RequestException as e:
    logging.error(f"Network Error : {e}")
    exit(1)


#print(response.status_code,response.text)

# 7️⃣ Iterate through the chunks as they arrive
for chunk in response.iter_lines(decode_unicode=True):  #“Keep giving me the next line of text from the server as soon as it arrives.”
    try:
        if not chunk or not chunk.startswith("data:"): #If nothing came yet (heartbeat/empty line), just wait again.
            continue

        line = chunk.strip()

        if chunk.startswith("data: "):  #Only pay attention to real data lines (SSE prefix)
            data_str = chunk[len("data: "):].strip() #Cut off the word data: so I’m left with pure JSON text
            if data_str == "[DONE]": #If the server says it’s done, stop listening.
                logging.info("Stream completed.")
                break

        try:
            data = json.loads(data_str) #Turn that text (JSON) into a Python dictionary
        except json.JSONDecodeError as je:
            logging.warning(f"Skipping malformed chunk: {je}")
            continue

        delta = data.get("choices",[{}])[0].get("delta",{}) #Reach into the dictionary to find the new partial content.
        content = delta.get("content") #Grab the actual text (the new word or phrase)

        if content:
            print(content, end = '', flush=True) #Show that text right now without waiting for the full reply
        
    except Exception as e:
        # Generic catch for unexpected runtime errors
        logging.exception(f"Error processing chunk: {e}")
        continue  # skip this chunk and keep streaming

print() #Move to the next line once the whole message is complete.
