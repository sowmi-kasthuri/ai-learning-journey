# 🌤️ Weather App

A simple command-line Weather App built as part of a daily coding practice challenge.  
Fetches live weather data based on the city entered by the user.

---

## ✨ Features

- Geocodes any city name to **latitude/longitude (in degrees)** using the **Open-Meteo Geocoding API**
- Retrieves current weather via the **Open-Meteo Forecast API**
- Handles:
  - Invalid city names  
  - Missing/null API results  
  - Network/API failures  
  - Cities with spaces (via URL encoding)
- Displays:
  - Temperature (°C)  
  - Windspeed (m/s)  
  - Weather code + human-readable description  
  - Location details (name, admin region, country)

---

## 🧭 Latitude & Longitude

- Units: **Decimal Degrees**
- Latitude range: **–90° to +90°**  
- Longitude range: **–180° to +180°**

**Example:**  
Chennai → latitude 13.0827°, longitude 80.2707°


---

## 🌥️ Weather Code Mapping (0–3)

| Code | Meaning         |
|------|-----------------|
| 0    | Clear sky       |
| 1    | Mainly clear    |
| 2    | Partly cloudy   |
| 3    | Overcast        |

---

## ▶️ How to Run

```bash
python weather_app.py
