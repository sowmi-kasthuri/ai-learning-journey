import os
import json
from datetime import datetime
from rich.console import Console

console = Console()

def export_answers(keyword:str, history_dir = "chat_history", export_dir = "exports"):
    """Search through saved chat history for a keyword and export Q&A pairs to Markdown."""

    os.makedirs(export_dir,exist_ok=True)
    export_file = f"{export_dir}/export_{keyword}_{datetime.now():%Y%m%d_%H%M%S}.md"

    collected = []

    for file in os.listdir(history_dir):
        if not file.endswith(".json"):
            continue

        path = os.path.join(history_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                console.print(f"[red]Error reading {file}: {e}[/red]")
                continue

        # Find user messages containing keyword and their assistant replies
        for i in range(len(data) - 1):
            msg, next_msg = data[i], data[i + 1]
            if (
                msg["role"] == "user"
                and keyword.lower() in msg["content"].lower()
                and next_msg["role"] == "assistant"
            ):
                collected.append(
                    f"### From {file}\n**Q:** {msg['content']}\n\n**A:** {next_msg['content']}\n\n---\n"
                )
    
    if collected:
        with open(export_file, "w", encoding="utf-8") as out:
            out.writelines(collected)
        console.print(f"[green]Exported {len(collected)} Q&A pairs to {export_file}[/green]")
        return export_file
    else:
        console.print(f"[yellow]No matches found for '{keyword}'.[/yellow]")
        return None