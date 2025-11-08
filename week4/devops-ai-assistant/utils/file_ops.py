##-----------------------------------
# 1️⃣ Import required files
##-----------------------------------
import os
import json

##-----------------------------------
# 2️⃣ Define Search chat history
##-----------------------------------
def search_chat_history(keyword, folder = 'chat_history'):
    results = []

    if not os.path.exists(folder):
        return ['No chat history found']
    
    for filename in os.listdir(folder):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(folder,filename)
        with open(path,"r",encoding="utf-8") as f:
            try:
                data = json.load(f)
                for msg in data:
                    if keyword.lower() in msg["content"].lower():
                        results.append(f"{filename}: [{msg['role']}] {msg['content']}")
            except Exception:
                continue
    return results if results else [f"No Matches found for '{keyword}'."]
            


