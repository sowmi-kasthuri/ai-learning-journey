# Fetch your GitHub repos and save them to a CSV using Pandas
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()
token = os.getenv('GITHUB_TOKEN')

# API endpoint
url = 'https://api.github.com/user/repos'
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Make the request
response = requests.get(url, headers=headers)

# check response
if response.status_code != 200:
    print("❌ Error:", response.status_code, response.text)

# parse json response
repos = response.json()

# Extract key info into a list of dicts
data = []
for repo in repos:
    data.append({
                "Name": repo["name"],
        "Full Name": repo["full_name"],
        "URL": repo["html_url"],
        "Private": repo["private"],
        "Language": repo.get("language", "N/A"),
        "Stars": repo["stargazers_count"],
        "Forks": repo["forks_count"],
        "Created At": repo["created_at"]
    })

# convert to dataframe
df = pd.DataFrame(data)

# save to csv
csv_file = 'github_repos.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')

print(f'✅ Saved {len(df)} repositories to {csv_file}')
print(df.head())
