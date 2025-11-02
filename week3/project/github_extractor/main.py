import os
import requests
import time
import json
import csv
from dotenv import load_dotenv
from datetime import datetime

# Load GitHub API token from root .env
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com/users/"

# Set headers for authenticated requests
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def fetch_repos(username, retries=3, backoff=2):
    """
    Fetch public repositories for a given GitHub username.
    Includes retry logic and timeout handling.
    """
    url = f"{BASE_URL}{username}/repos"
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(backoff ** attempt)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error: {e}")
            break
    return None

def save_data(username, repos):
    """
    Save repository data to CSV and JSON with timestamped filenames.
    """
    if not repos:
        print("No data to save.")
        return

    os.makedirs("week3/project/github_extractor/data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"week3/project/github_extractor/data/{username}_repos_{timestamp}.csv"
    json_path = f"week3/project/github_extractor/data/{username}_repos_{timestamp}.json"

    # Prepare data
    fields = ["name", "stargazers_count", "forks_count", "language", "updated_at"]
    simplified = [{field: repo.get(field, None) for field in fields} for repo in repos]

    # Write CSV
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(simplified)

    # Write JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(simplified, f, indent=4)

    print(f"✅ Data saved to:\n  {csv_path}\n  {json_path}")

def main():
    username = input("Enter GitHub username: ").strip()
    repos = fetch_repos(username)
    if repos:
        print(f"Fetched {len(repos)} repositories for {username}")
        save_data(username, repos)
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
