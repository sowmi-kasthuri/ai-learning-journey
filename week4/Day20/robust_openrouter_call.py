import os, requests, time, logging
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')
url = "https://openrouter.ai/api/v1/chat/completions"

# Configure logging
logging.basicConfig(
    filename="openrouter.log", # log file path
    level=logging.INFO,  # log level (INFO, ERROR, DEBUG)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content_Type":"application/json"
}

def call_openrouter(prompt, retries=3, backoff=2):
    data = {
        #"model":"openai/gpt-3.5-turbo",
        "model":"openai/gpt-3.5-turbo",
        "messages": [{"role":"user", "content":prompt}]
    }

    for attempts in range(1, retries + 1):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=10)

            response.raise_for_status()  # Raise exception for bad status (4xx/5xx)

            return response.json()["choices"][0]["message"]["content"] # If successful, return response
            
        except requests.exceptions.HTTPError as http_err:
            status = response.status_code if response else None

            # Retry only for temporary errors (5xx, 429)
            if status and (500 <= status <= 600):
                print(f"HTTP {status} error, will retry : {http_err}")
                logging.warning(f"HTTP {status} error, will retry : {http_err}")
            else:
                print(f"Non-retriable HTTP error : {http_err}")
                logging.error(f"Non-retriable HTTP error : {http_err}")
                break  # don't retry on permanent errors (400, 401, 403, etc.)

        
        except requests.exceptions.RequestException as err:
            print(f"Attempt {attempts} : failed {err} ")
            logging.error(f"Attempt {attempts} : failed {err} ")  # Network errors like timeouts, DNS, etc.

        if attempts <  retries:
            sleep_time = backoff ** attempts
            print(f"Retrying in {sleep_time} seconds...")
            logging.warning(f"Retrying in {sleep_time} seconds...")
            time.sleep(sleep_time)
        else:
            print("❌ All retries failed")
            logging.error("❌ All retries failed")

if __name__ == "__main__":
    user_prompt = input("Ask anything : ")
    print(call_openrouter(user_prompt))
