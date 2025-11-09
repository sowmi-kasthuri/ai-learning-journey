# utils/semantic_ops.py
import os
import json
import numpy as np

from sentence_transformers import SentenceTransformer, util
from rich.console import Console

console = Console()
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_search(query, history_dir="chat_history", top_n=5):
    """Find semantically similar Q&A pairs for the given query."""
    qa_pairs = []

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
        
        for i in range(len(data) - 1):
            msg, next_msg = data[i], data[i + 1]
            if msg["role"] == "user" and next_msg["role"] == "assistant":
                qa_pairs.append(f"Q: {msg['content']} A: {next_msg['content']}")
    
    if not qa_pairs:
        console.print("[yellow]No saved chats to search semantically.[/yellow]")
        return []
    
    console.print(f"[dim]Encoding {len(qa_pairs)} Q&A pairs...[/dim]")
    qa_embeds = model.encode(qa_pairs, convert_to_tensor=True)
    query_embed = model.encode(query, convert_to_tensor=True)

    scores = util.cos_sim(query_embed, qa_embeds)[0]
    top_indices = np.argsort(-scores)[:top_n]

    results = []
    for idx in top_indices:
        score = float(scores[idx])
        results.append((score, qa_pairs[idx]))

    console.print(f"[green]Top {top_n} semantic matches:[/green]")
    for s, text in results:
        console.print(f"[dim]{round(s,3)}[/dim] {text[:200]}...\n")

    return results