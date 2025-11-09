# assistant.py (drop-in replacement)
import os
import json
from datetime import datetime
import requests
from rich.console import Console

# imports from your utils
from utils.file_ops import search_chat_history
from utils.config import OPENROUTER_API_URL, MODEL, HEADERS
from utils.memory import ConversationMemory
from utils.export_ops import export_answers
from utils.semantic_ops import semantic_search

console = Console()
memory = ConversationMemory("You are a DevOps expert assistant.")

def save_chat_history(memory_obj):
    if not getattr(memory_obj, "history", None):
        console.print("[yellow]⚠️ No conversation to save[/yellow]")
        return
    
    os.makedirs("chat_history", exist_ok=True)
    filename = f"chat_history/session_{datetime.now():%Y%m%d_%H%M%S}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(memory_obj.history, f, indent=2)
    console.print(f"[green]💾 Chat saved to {filename}[/green]")

def pretty_print_results(results):
    """Normalize and print results from search_chat_history for debugging."""
    if not results:
        console.print("[dim]Search helper returned empty list[/dim]")
        return False
    
    # If function returned a single string like "No matches for 'X'." treat as no-results
    if isinstance(results, list) and len(results) == 1 and isinstance(results[0], str):
        if "no match" in results[0].lower() or "no matches" in results[0].lower():
            console.print(f"[dim]{results[0]}[/dim]")
            return False
    
    # Otherwise print entries
    for r in results[:10]:
        console.print(f"[green]- {r}[/green]")
    return True

def call_ai_and_record(user_text):
    """Call OpenRouter and add result to memory. Returns True if successful."""
    memory.add("user", user_text)
    payload = {"model": MODEL, "messages": memory.history}
    
    # debug print
    console.print(f"[blue][debug][/blue] Calling AI with model={MODEL} and user_text='{user_text}'")
    try:
        resp = requests.post(OPENROUTER_API_URL, headers=HEADERS, json=payload, timeout=45)
        console.print(f"[blue][debug][/blue] HTTP status: {resp.status_code}")
        # print raw response text if not JSON - helps debug
        try:
            data = resp.json()
        except Exception:
            console.print(f"[red]Non-JSON response:[/red] {resp.text[:400]}")
            return False

        # defensive access into response structure
        choices = data.get("choices") or []
        if not choices:
            console.print(f"[red]No choices in response JSON: {data}[/red]")
            return False
        
        message = choices[0].get("message") or {}
        ai_message = message.get("content") or ""
        if not ai_message:
            console.print(f"[red]AI message empty in response: {data}[/red]")
            return False

        console.print(f"[cyan]AI:[/cyan] {ai_message}\n")
        memory.add("assistant", ai_message)
        return True

    except Exception as e:
        console.print(f"[red]Error calling AI:[/red] {e}")
        return False

def main():
    console.print("[bold cyan]DevOps AI Assistant[/bold cyan]")
    console.print("[dim]Type 'exit' to quit. Try: 'search docker' or just 'docker'[/dim]\n")

    while True:
        user_input = console.input("[yellow]You:[/yellow] ").strip()
        if not user_input:
            continue

        # exit
        if user_input.lower() in ["exit", "quit"]:
            save_chat_history(memory)
            break

        # detect search command (case-insensitive)
        parts = user_input.strip().split(" ", 1)
        if len(parts) > 1 and parts[0].lower() == "search":
            keyword = parts[1].strip()
            console.print(f"[dim]Searching for '{keyword}' in past sessions...[/dim]")
            results = search_chat_history(keyword)

            # debug show raw results type/len
            console.print(f"[blue][debug][/blue] search_chat_history returned type={type(results)} len={len(results) if hasattr(results,'__len__') else 'n/a'}")

            found = pretty_print_results(results)
            if found:
                # found hits — skip live AI
                continue
            else:
                # NO hits — fallback to live AI using the keyword (not the original 'search X')
                console.print(f"[dim]No prior matches found. Falling back to live AI for: '{keyword}'[/dim]")
                # Call AI with the keyword and record result
                ok = call_ai_and_record(keyword)
                if not ok:
                    console.print("[red]AI call failed during search fallback.[/red]")
                continue
        
        # ---- export command ----
        if user_input.lower().startswith("export "):
            keyword = user_input.split(" ", 1)[1].strip()
            console.print(f"[dim]Exporting all chat entries related to '{keyword}'...[/dim]")
            save_chat_history(memory)
            export_answers(keyword)
            continue
    
        # ---- semantic search command ----
        if user_input.lower().startswith("semantic search "):
            query = user_input.split(" ", 2)[2].strip()
            console.print(f"[dim]Performing semantic search for '{query}'...[/dim]")
            semantic_search(query)
            continue
               
        # If not a 'search' command, treat input as normal question
        ok = call_ai_and_record(user_input)
        if not ok:
            console.print("[red]Failed to get AI response for your query.[/red]")

if __name__ == "__main__":
    main()
