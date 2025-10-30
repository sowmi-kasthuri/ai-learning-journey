import requests, json, os
import pandas as pd
from datetime import datetime

# create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Create folder if it doesn’t exist
os.makedirs("github_repos", exist_ok=True)

# prompt for username
username = input("Enter GitHub username: ")

# dynamic filenames
csv_file = f"github_repos/{username}_repos_{timestamp}.csv"
json_file = f"github_repos/{username}_repos_{timestamp}.json"

# Build API URL
url = f"https://api.github.com/users/{username}/repos"

# fetch the data
response = requests.get(url)
data = response.json()
# print(json.dumps(data,indent=2))

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

# Push the semi-flat structure to a data frame
repos = sorted(repos, key=lambda u:u['name']) #Sort users by name . for fun.
df = pd.DataFrame(repos)
# print(df)

# Push to a CSV
df.to_csv(csv_file,index=False)
df.to_json(json_file, orient="records", indent=2)


print(f"✅ Saved files in outputs/{csv_file} and outputs/{json_file}")