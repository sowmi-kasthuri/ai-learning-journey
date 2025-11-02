import requests
import time


def get_weather(city, retries=3, delay=2):
    """Fetch weather data for a given city with retry + error handling."""
    api_key = "71c4e39d277c395ea4a42ad96d964cad"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # raise HTTPError for bad responses
            data = response.json()

            # ✅ consistent structured return
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
            }

        except requests.exceptions.Timeout as e:
            print(f"Attempt {attempt + 1}: Timeout occurred — {e}")
        except requests.exceptions.ConnectionError as e:
            print(f"Attempt {attempt + 1}: Connection error — {e}")
        except requests.exceptions.HTTPError as e:
            print(f"Attempt {attempt + 1}: HTTP error — {e}")
            return {"error": "City not found or bad request"}
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1}: General request error — {e}")

        time.sleep(delay)

    print("All retry attempts failed.")
    return None


if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city)) #
