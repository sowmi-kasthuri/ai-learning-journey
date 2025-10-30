import requests, json, os
import pandas as pd
from datetime import datetime

url = 'https://randomuser.me/api/?results=10'

# create timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# Create folder if it doesn’t exist
os.makedirs("github_repos", exist_ok=True)

# dynamic filenames
csv_file = f"outputs/users_{timestamp}.csv"
json_file = f"outputs/users_{timestamp}.json"

# fetch the data
response = requests.get(url)
data = response.json()
#print(json.dumps(data,indent=2)) # just shows a pretty dump of json

# Extract key details of user data
'''
for user in data['results']:
    first = user['name']['first']
    last = user['name']['last']
    city = user['location']['city']
    email = user['email']
    print(f'{first} {last} | {city} | {email}')
'''

users = [
    {
        "name" : f"{u['name']['first']} {u['name']['last']}",
        "email" : u["email"],
        "city" : u["location"]["city"],
        "country" : u["location"]["country"]
    }
    for u in data["results"]
]

#print(json.dumps(users, indent=2,sort_keys=True)) 

# Push the semi-flat structure to a data frame
users = sorted(users, key=lambda u:u['name']) #Sort users by name . for fun.
df = pd.DataFrame(users)
print(df) # print flat structure

# Push to a CSV
df.to_csv(csv_file,index=False)
df.to_json(json_file, orient="records", indent=2)


print(f"✅ Saved files in outputs/{csv_file} and outputs/{json_file}")


