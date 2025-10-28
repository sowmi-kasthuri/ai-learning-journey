# URL - https://api.openweathermap.org/data/2.5/weather

import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
city = "Perungalathur"
url = "https://api.openweathermap.org/data/2.5/weather"

# Example 1. Query Parameter based authentication.  Creds sent in URL
'''
params = {"q":city, "appid":api_key, "units":"metric"}

response = requests.get(url,params=params)
# print(response.status_code, response.text)

if response.status_code != 200:
    print("Error:", response.status_code, response.text)
else:
    data = response.json()
    #print(data)
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Min. Temp: {data['main']['temp_min']}°C")
    print(f"Max. Temp: {data['main']['temp_max']}°C")
    print(f"Feels Like: {data['main']['feels_like']}°C")
    print(f"Humidity: {data['main']['humidity']}°C")
    print(f"Condition: {data['weather'][0]['description'].title()}")
    
'''

# Example 2. Header based authentication . creds sent in header
'''
params = {'q':city, 'units':'metric'}
headers = {'x-api-key': api_key}
response = requests.get(url,headers=headers,params=params)
print(response.status_code)
print(response.text)
'''

# Example 3. GitHub Bearer token based auth.  Connect to github and display the repos
token = os.getenv('GITHUB_TOKEN')
github_url = 'https://api.github.com/user'
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json'
}
response = requests.get(github_url,headers=headers)
if response.status_code == 200:
    data = response.json()
    print(f"✅ Authenticated as: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
    
    github_repo = 'https://api.github.com/user/repos'
    repo_response = requests.get(github_repo,headers=headers)
    repos = repo_response.json()

    for repo in repos:
        print(repo['name'], ' - ', repo['html_url'])
else:
    print("❌ Error:", response.status_code, response.text)
