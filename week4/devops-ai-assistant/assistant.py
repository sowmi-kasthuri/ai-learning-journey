#-----------------------------------
# 1️⃣ Import required files
#-----------------------------------
import os
import json
from datetime import datetime
import requests
from dotenv import load_dotenv
from rich.console import Console
from utils.file_ops import search_chat_history

#-----------------------------------
# 2️⃣ - Load env
#-----------------------------------
console = Console()
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
api_url = os.getenv("OPENROUTER_API_URL")
model = os.getenv("MODEL")

#-----------------------------------
# 3️⃣ - Create header 
#-----------------------------------

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json",
    "HTTP-Referer": "https://openrouter.ai/",
    "X-Title": "DevOps AI Assistant"
}

#-----------------------------------
# 4️⃣ - Init conversation
#-----------------------------------
conversation = [
    {"role": "system", "content": "You are a DevOps expert assistant. Keep answers practical and short."},
]

#-----------------------------------
# 5️⃣ - helper: save chat history
#-----------------------------------
def save_chat_history(history):
    if not history:
        console.print("[yellow]⚠️ No conversation to save[/yellow]")
        return
    
    os.makedirs("chat_history",exist_ok=True)
    filename = f"chat_history/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(history,f,indent=2)
    console.print(f"[green]💾 Chat saved to {filename}[/green]")


#-----------------------------------
# 5️⃣ - main loop
#-----------------------------------
def main():
    console.print("[bold cyan]DevOps AI Assistant[/bold cyan]")
    console.print("[dim]Type 'exit' to quit.[/dim]\n")

    while True:
        user_input = console.input("[yellow]You:[/yellow] ").strip()
        if user_input.lower() in ["exit","quit"]:
            save_chat_history(conversation)
            break

#-----------------------------------
# 6️⃣ - Search command handling
#-----------------------------------
        cmd = user_input.strip().split(" ",1)
        if len(cmd) > 1 and cmd[0].lower() == 'search':
            keyword = cmd[1]
            console.print(f"[dim]Searching for '{keyword} in past sessions...[/dim]")
            results = search_chat_history(keyword)
            for r in results[:10]: #limit to first 10 results
                console.print(f"[green] - {r} [/green]")
            continue

        conversation.append({"role":"user","content":user_input})


        payload = {
            "model":model,
            "messages":conversation
        }

#-----------------------------------
# 7️⃣ - Perform standard LLM search
#-----------------------------------
        try:
            response = requests.post(api_url, headers=headers, json=payload, timeout=45)
            data = response.json()

            ai_message = data["choices"][0]["message"]["content"]
            console.print(f"[cyan]AI:[/cyan] {ai_message}\n")

            conversation.append({"role":"assistant", "content":ai_message})

        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")

#-----------------------------------
# 8️⃣ - Call main
#-----------------------------------
if __name__ == "__main__":
    main()