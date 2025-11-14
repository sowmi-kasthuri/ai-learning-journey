import urllib.request
import urllib.parse
import json

while True:
    city = input("\nEnter city (or 'exit'): ").strip()
    
    if city.lower() in ("exit","quit","q"):
        print("Good Bye !!!!")
        break

    print(f"City entered is {city}")

    city_encoded = urllib.parse.quote(city)
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_encoded}&count=1"

    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode("utf-8"))

        if not data.get("results"):
            print("City not found")
            continue

        latitude = data["results"][0]["latitude"]
        longitude = data["results"][0]["longitude"]

        print(f"latitude / longitude of {city} : {latitude} / {longitude}")

        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}&current_weather=true"
            )

        weather_response = urllib.request.urlopen(weather_url)
        weather_data = json.loads(weather_response.read().decode("utf-8"))
        weather_code_map = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast"
            }
        
        current_weather = weather_data["current_weather"]
        temp = current_weather["temperature"]
        wind = current_weather["windspeed"]
        code = current_weather["weathercode"]
        code_description = weather_code_map.get(code,"Unknown")
        time = current_weather["time"]

        print(f" ----- Current Weather in {city} ------\n")
        print(f"Temperature : {temp}°C")
        print(f"Windspeed   : {wind} m/s")
        print(f"WeatherCode : {code_description}")
        print(f"Time        : {time}")

    except Exception as e:
        print(f"Network or API error - {e}") 
