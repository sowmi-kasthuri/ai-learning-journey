##--------------------------------------------------------------------
# 1️⃣ This is the config file that stores the openrouter configuration
##--------------------------------------------------------------------

import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = os.getenv("OPENROUTER_API_URL")
MODEL = os.getenv("MODEL", "meta-llama/llama-3.1-70b-instruct")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type":"application/json",
    "Http-Referer":"https://openrouter.ai/",
    "X-Title":"DevOps AI Assistant"
}