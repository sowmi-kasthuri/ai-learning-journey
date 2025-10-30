import requests, json, os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# 1️⃣ Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# 2️⃣ Cities to check
cities = ["Hyderabad", "Chennai", "Pune"]

# 3️⃣ Setup folder + timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M")
os.makedirs("weather_reports", exist_ok=True)
csv_file = f"weather_reports/cities_{timestamp}.csv"
json_file = f"weather_reports/cities_{timestamp}.json"

# 4️⃣ Empty list to store city data
weather_data = []

# 5️⃣ Loop through cities
for city in cities:
    # build URL
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    # fetch data
    response = requests.get(url)
    data = response.json()
    #print(json.dumps(data,indent=2))
 
 
    # extract key fields into a dict
    city_info = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": timestamp
    }
    #print(city_info)

    # append to list
    weather_data.append(city_info)

# 6️⃣ Save to JSON + CSV
with open(json_file, "w") as f:
    json.dump(weather_data, f, indent=2)

df = pd.DataFrame(weather_data)
df.to_csv(csv_file, index=False)

print("Weather data saved successfully!")
