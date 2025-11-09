# DevOps AI Assistant 🤖

🧩 PROJECT SUMMARY — DevOps AI Assistant
🎯 Goal

Build a personal DevOps helper that:

Answers infra / DevOps questions (via AI)
Remembers past sessions
Searches past solutions
Exports Q&A answers
Supports semantic (meaning-based) recall

🏗️ Project Structure
devops-ai-assistant/
├── assistant.py              ← Main CLI orchestrator
├── .env                      ← Contains OPENROUTER_API_KEY, MODEL, URL
├── requirements.txt
├── chat_history/             ← Auto-saved chat sessions (JSON)
├── exports/                  ← Markdown exports & semantic results
└── utils/
    ├── config.py             ← API keys, headers, constants
    ├── memory.py             ← ConversationMemory class
    ├── file_ops.py           ← Chat search utilities
    ├── export_ops.py         ← Export logic (keyword-based Q&A)
    └── semantic_ops.py       ← Semantic search via embeddings

✅ Features Completed
Feature	Description	Status
Core Assistant Loop	Handles input → AI → output	✅
Persistent Memory	Saves session JSON automatically	✅
Keyword Search	Finds answers by term match	✅
Export	Creates Markdown Q&A dump	✅
Semantic Search	Finds answers by meaning (embeddings)	✅
Refactor	Modular utils-based architecture	✅
Error Handling	Graceful warnings, fallback to AI	✅
🧠 Tech Stack

Language: Python 3.10+

Libraries:
openai, requests, python-dotenv, rich, sentence-transformers, numpy

LLM Backend: OpenRouter API (GPT-4-mini)

Embedding Model: all-MiniLM-L6-v2

💡 Key Learnings
Structured modular design — config, utils, and main separated cleanly.
How to persist and reload conversations as JSON.
Using embeddings to search by meaning, not just keywords.
File operations, data handling, and error-safe AI loops.
Practical application of RAG-lite techniques.


## 🚀 How to Run

```bash
pip install -r requirements.txt
python assistant.py
