from openai import OpenAI
from dotenv import load_dotenv
import os

# Load Environment and Client
load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL")
)

# Define system prompt AI's personality
system_prompt = """
You are a witty but out of work DevOps Engineer with 20+ years of experience.  
You explain cloud and CI/CD concepts with humor and short shell examples.
All the while give life examples and motivations.
"""

# Define question
question = "Explain Docker in few sentences"

for temp in [0, 1]:
    print(f"\n=== Temperature: {temp} ===\n")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=temp,
        max_output_tokens=150
    )

    print(response.output_text)