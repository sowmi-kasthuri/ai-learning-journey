import time
import os
from groq import Groq
from dotenv import load_dotenv
import httpx
from fastapi import HTTPException

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# placeholder adapters — we wire Groq/OpenRouter later
async def call_llm(prompt: str, model: str="groq"):
    start = time.time()

    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    try:    

        response = client.chat.completions.create(
            model = model_name,
            messages = [{"role": "user", "content": prompt}]
        )
    except httpx.RequestError as e:
         # network, DNS, timeout, connection issues
         raise HTTPException(status_code=503, detail=f"Groq network error: {str(e)}")    
    text = response.choices[0].message.content
    tokens = response.usage.total_tokens if response.usage else 0
    latency_ms = int((time.time() - start)*1000)
    
    return {
        "text": text,
        "tokens": tokens,
        "latency_ms": latency_ms
    }