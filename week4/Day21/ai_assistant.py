from openai import OpenAI
from dotenv import load_dotenv
import os, time

# Load env + client
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL")
)

# System prompt - AI Personality definition
system_prompt = """
You are a witty but out of work DevOps Engineer with 20+ years of experience.
You explain cloud and CI/CD concepts with humor and short shell examples.
All the while give life examples and motivations.
"""

# Conversation memory
conversation = [{"role":"system", "content":system_prompt}]

# main chat loop
while True:
    user_input = input("You : ")

    if user_input.lower() in ["exit","quit"]:
        print("!!! 👋 Good Bye 👋 !!!")     
        break

    conversation.append({"role":"user", "content":user_input})

    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                input = conversation,
                temperature = 0.5,
                max_output_tokens=300
            )
            break #Success + break retry

        except Exception as e:
            wait = 2**attempt #exponential backoff
            print(f"Error: {e}\n ⏳ Retrying in {wait}s...")
            time.sleep(wait)
    
    else:
        print(" Failed after multiple tries.  Please try again later...")
        continue

    ai_reply = response.output_text
    print(f"\n Assistant : {ai_reply}\n")

    conversation.append({"role":"assistant", "content":ai_reply})


