from dotenv import load_dotenv
import os
import requests
import time
import logging

# --------------------------------------------------
# Setup logging (file + console)
# --------------------------------------------------
logging.basicConfig(
    filename="ai_comparer.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S"))
logging.getLogger().addHandler(console)

# --------------------------------------------------
# Load API keys
# --------------------------------------------------
load_dotenv()
api_url = os.getenv("OPENAI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")

if not api_key or not api_url:
    raise SystemExit("❌ Missing OPENAI_API_KEY or OPENAI_BASE_URL in .env")

# --------------------------------------------------
# Ask OpenRouter (single function for both models)
# --------------------------------------------------

def ask_openrouter(model, question):
    headers = {
        "Authorization":f"Bearer {api_key}",
        "Content-Type":"application\json"
    }

    payload = {
        "model":model,
        "messages":[
            {"role": "system", "content": "Answer briefly in one sentence."},
            {"role": "user", "content": question}
        ],
        "temperature":0.25,
    }
    # model-specific token limits
    if "claude" in model:
        payload["max_output_tokens"] = 40    # Anthropic format
    else:
        payload["max_completion_tokens"] = 50  # OpenAI / GPT format

    start = time.perf_counter()
    try:
        r = requests.post(f"{api_url}/chat/completions", headers=headers, json=payload, timeout=45)
        r.raise_for_status()
        elapsed = time.perf_counter() - start

        data = r.json()
        text = data["choices"][0]["message"]["content"].strip()
        usage = data.get("usage",{})

        if not text:
            print("No Text returned...")

        logging.info(f"{model} succeeded in {elapsed:.2f}s | Tokens = {usage.get('tokens',' - ')}")
        return {"ok":True, "text":text, "elapsed":elapsed, "usage": usage}
    
    except Exception as e:
        elapsed = time.perf_counter() - start
        logging.error(f"{model} failed after {elapsed:.2f}s → {type(e).__name__}: {e}")
        return {"ok":False, "text":"", "elapsed":elapsed, "usage":{}, "error":str(e)}

# --------------------------------------------------
# Main Program
# --------------------------------------------------
if __name__=="__main__":
    print("\n===== Dual AI Comparer =====\n")
    question = input("Enter your question: ").strip()

    if not question:
        print("No Question Asked....exiting")
        exit()
    
    models = {
        "OpenAI GPT-4o-mini": "gpt-4o-mini",
        "Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet"
    }

    results = {}

    logging.info("\nCalling models via OpenRouter...\n")

    for name, model in models.items():
        print(f"Asking {name}.....\n")
        result = ask_openrouter(model, question)
        results[name] = result

        if result["ok"]:
            logging.info(f"✅ {name} done in {result['elapsed']:.2f}s\n")
        else:
            logging.error(f"❌ {name} failed: {result['error']}")
# --------------------------------------------------
# Compare Results
# --------------------------------------------------
    print("\n" + "=" * 80)
    print("RESULTS COMPARISON".center(80))
    print("=" * 80 + "\n")

    for name, data in results.items():
        print(f"### {name} ###")
        if data["ok"]:
            print(f"⏱ Time: {data['elapsed']:.2f}s")
            print(f"📊 Usage: {data['usage']}")
            print(f"\n🧠 Response:\n{data['text']}\n")
        else:
            print(f"❌ Error: {data['error']}\n")
        print("-" * 80)

    logging.info("Comparison completed successfully.\n")
