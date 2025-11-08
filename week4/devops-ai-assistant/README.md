# DevOps AI Assistant 🤖

Your personal DevOps helper — built using OpenRouter API and Python.

Ask infrastructure questions, get AI troubleshooting help, and save your chat history automatically.

---

## ⚙️ Features

✅ Ask DevOps questions (AWS, Docker, K8s, CI/CD, Terraform, etc.)  
✅ AI responds with short, practical solutions  
✅ Persistent conversation memory (per session)  
✅ Saves all chats as JSON files in `chat_history/`  
✅ Configurable model and API key via `.env`

*(Coming soon)*  
🔍 Search past solutions  
📤 Export specific answers  
🧠 Different modes: AWS / Docker / K8s  

---

## 🏗️ Project Structure

devops-ai-assistant/
├── assistant.py # main entry point
├── utils/
│ ├── memory.py # (future) memory utilities
│ ├── file_ops.py # (future) search/export functions
│ └── config.py # (future) config loader
├── chat_history/ # saved chat sessions
├── .env # OpenRouter API key + model
├── requirements.txt
└── README.md


---

## 🚀 Setup Instructions

### 1. Clone & Create Virtual Environment
```bash
git clone <repo_url>
cd devops-ai-assistant
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # macOS/Linux

2. Install Dependencies
pip install -r requirements.txt

3. Add Environment Variables
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_API_URL=https://openrouter.ai/api/v1/chat/completions
MODEL=meta-llama/llama-3.1-70b-instruct

4. Run the Assistant
python assistant.py

Example session:
You: How to restart a failed pod in Kubernetes?
AI: You can delete the pod; the ReplicaSet or Deployment will recreate it automatically.
You: exit
💾 Chat saved to chat_history/session_20251108_173344.json


💡 Tips
Always run the script from the project root, where .env exists.
Type exit or quit to end the session and save your chat.
All conversations are stored as timestamped JSON files under chat_history/.

🧰 Requirements
Python 3.9+
Internet access
OpenRouter account with an API key (Free)

🧭 Next Up
 Implement live streaming responses
 Add search through previous sessions
 Support multiple “modes” (e.g., AWS, Docker, K8s)
 Optional Markdown export of key answers

 🧑‍💻 Author
Built by Sowmi as part of the Week 4 Weekend Project — AI + DevOps Integration Challenge.