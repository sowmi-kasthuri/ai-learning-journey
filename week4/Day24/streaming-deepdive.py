import os
import requests
import logging
import time
import json

# 1️⃣ load env
from dotenv import load_dotenv
load_dotenv()
#print("DEBUG URL:", os.getenv("OPENROUTER_API_URL"))

url = os.getenv("OPENROUTER_API_URL")
key = os.getenv("OPENROUTER_API_KEY")
model = os.getenv("MODEL")
temperature = float(os.getenv("TEMPERATURE","0.2"))
max_tokens = float(os.getenv("MAX_TOKENS","100"))



# 2️⃣ set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
   # handlers=[logging.FileHandler("streaming.log"), logging.StreamHandler()]
)


# 3️⃣ ask question
#question = input("You : ")



# 4️⃣ build json payload
payload = {
    "model":model,
    "messages":[
       # {"role":"system", "content":"Answer in one or two sentences"},
        {"role":"user", "content":"Stream this message word by word" }
        ],
    "stream":True,
    "temperature":temperature,
    "max_tokens":max_tokens
}


# 5️⃣ set headers - Bearer auth
headers = {
    "Authorization":f"Bearer {key}",
    "Content-Type":"application/json"
}


# 6️⃣Stream response
start = time.time()
with requests.post(url, headers=headers, json=payload, stream=True) as resp:
    resp.raise_for_status()

    for line in resp.iter_lines(decode_unicode=True):
        if not line or not line.startswith("data: "):
            if line:
                print("RAW:", line)

logging.info(f"\nTotal time: {time.time() - start:.2f}s")

