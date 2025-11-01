import os
import requests
import csv
from datetime import datetime
from dotenv import load_dotenv
from requests.exceptions import RequestException, Timeout

load_dotenv()

API_URL = os.getenv("EXCHANGE_API_URL", "https://open.er-api.com/v6/latest")

def get_exchange_rate(base_currency, target_currency, retries=3, timeout=5):
    for attempt in range(1, retries + 1):
        try:
            print("Using API URL:", API_URL)
            response = requests.get(f"{API_URL}/{base_currency.upper()}", timeout=timeout)
            response.raise_for_status()
            data = response.json()

            if "rates" in data and target_currency.upper() in data["rates"]:
                return data["rates"][target_currency.upper()]
            else:
                print("Unexpected response format:", data)
                return None

        except Timeout:
            print(f"Timeout on attempt {attempt}/{retries}. Retrying...")
        except RequestException as e:
            print(f"Error: {e}. Retrying ({attempt}/{retries})...")

    return None



def log_to_csv(base_currency, target_currency, rate, filename="exchange_log.csv"):
    """Log each exchange rate lookup to a CSV file."""
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), base_currency, target_currency, rate])
