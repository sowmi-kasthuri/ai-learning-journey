from dotenv import load_dotenv
import os

load_dotenv()
# print(os.getenv("OPENAI_API_KEY"))
messages = [
    {
        "role":"system",
        "content":"you are a helpful assistant"
    }
]
user_input = input("Ask Something : ")
messages.append({"role":"user","content":user_input})

import requests

headers = {
    "Authorization":f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
    "Content-Type":"application/json"
}

data = {
    "model":"gpt-3.5-turbo",
    "messages":messages
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

try:
    resp = response

    if resp.status_code == 200:
        reply = resp.json()["choices"][0]["message"]["content"]
        print("AI -- ", reply)
    else:
        try:
            err = resp.json()
            msg = err.get("error",{}).get("message") or err
        except ValueError:
            msg = resp.text
        print(f"Error -- {resp.status_code} : {msg}")
except requests.exceptions.RequestException as e:
    print("Network Error -- ", str(e))