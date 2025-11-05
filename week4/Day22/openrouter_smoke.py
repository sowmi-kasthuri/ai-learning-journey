# Day 22 - OpenRouter API Smoke Test
# Purpose: verify .env loading and OpenRouter connectivity

from dotenv import load_dotenv
import os, requests, time

# 1️⃣ Load .env from current folder
load_dotenv()

# 2️⃣ Read variables
api_key = os.getenv("OPENAI_API_KEY")
api_url = os.getenv("OPENAI_BASE_URL")

if not api_key or not api_url:
    raise SystemExit("❌ Missing OPENAI_API_KEY or OPENAI_BASE_URL in .env")

# 3️⃣ Function to call OpenRouter
def ask_openrouter(model,question):
    headers = {
        "Authorization":f"Bearer {api_key}",
        "Content-Type":"application/json",
        "X-Title":"Day 22 smoke test"
    }
    payload = {
        "model":model,
        "messages":[{"role":"user","content":question}]
    }
    
    start = time.perf_counter()
    response = requests.post(f"{api_url}/chat/completions",headers=headers,json=payload,timeout=30)
    elapsed = time.perf_counter() - start

    response.raise_for_status()
    data = response.json()
    text = data["choices"][0]["message"]["content"]
    usage = data.get("usage")
    return text, elapsed, usage

# 4️⃣ Run a test call
if __name__ == "__main__":
    question = "Hello! Please confirm you are responding via OpenRouter."
    print(f"Asking model: gpt-4o-mini\nQuestion: {question}\n")

    try:
        text, elapsed, usage = ask_openrouter("gpt-4o-mini", question)
        print(f"Response received in {elapsed}s..\n")
        print(f"Response : \n",text)
        print(f"\n Usage : \n ",usage)
    except Exception as e:
        print("❌ ERROR:",e)