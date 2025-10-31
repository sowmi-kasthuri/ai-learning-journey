import requests, json, os, time
import pandas as pd
from datetime import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)



# create timestamp ----- Setup ----
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# prompt for username
username = input(Fore.CYAN +"Enter GitHub username: ").strip()
os.makedirs("github_repos", exist_ok=True)
csv_file = f"github_repos/{username}_repos_{timestamp}.csv"
json_file = f"github_repos/{username}_repos_{timestamp}.json"


# ---- Retry + Timeout Setup ----
session = requests.Session()
retry_strategy = Retry(
    total=3,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)


# Build API URL
url = f"https://api.github.com/users/{username}/repos"

# fetch the data
try:
    print(Fore.YELLOW + f"Fetching repos for: {username} ...")
    response = session.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    time.sleep(2)  # rate limit
except requests.exceptions.Timeout:
    print(Fore.RED + "❌ Request timed out. Try again later.")
    exit()
except requests.exceptions.HTTPError as e:
    print(Fore.RED + f"❌ HTTP error: {e}")
    exit()
except requests.exceptions.RequestException as e:
    print(Fore.RED + f"❌ Network error: {e}")
    exit()



# extract key details from the repo
repos = [
    {
        "name" : r["name"],
        "language" : r["language"],
        "stargazers_count" : r["stargazers_count"],
        "updated_at" : r["updated_at"],
        "html_url" : r["html_url"]        
    }
    for r in data
]
# print(json.dumps(repos, indent=2,sort_keys=True)) 

# ---- Save Outputs ----
if repos:
    pd.DataFrame(repos).to_csv(csv_file, index=False)
    with open(json_file, "w") as f:
        json.dump(repos, f, indent=2)
        print(Fore.GREEN + f"✅ Success! Saved {len(repos)} repos")
        print(Style.DIM + f"📄 CSV: {csv_file}\n📘 JSON: {json_file}")
else:
    print(Fore.RED + "⚠️  No repositories found or invalid user.")