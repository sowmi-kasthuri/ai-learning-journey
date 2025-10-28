# URL - https://api.openweathermap.org/data/2.5/weather

import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")
city = "Perungalathur"

url = "https://api.openweathermap.org/data/2.5/weather"
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
    

