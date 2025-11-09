##--------------------------------------------------------------------
# 1️⃣ Session memory management
##--------------------------------------------------------------------
'''
🧩 Purpose - Handle in-memory chat context during a session — 
maybe with limits, summarization, or trimming old messages.
'''

import json
import os
from datetime import datetime

class ConversationMemory:
    def __init__(self, system_prompt):
        self.history = [{"role":"system", "content":system_prompt}]

    def add(self, role, content):
        self.history.append({"role":role, "content":content})

    def trim(self, limit = 10):
        if len(self.history) > limit + 1:
            self.history = [self.history[0] + self.history[-limit:]]
    
    def save(self, folder = "chat_history"):
        os.makedirs(folder, exist_ok=True)
        filename = f"{folder}/session_{datetime.now():%Y%m%d_%H%M%S}.json"
        with open(filename,"w",encoding="utf-8") as f:
            json.dump(self.history, f, indent=2)
        return filename