import requests
from all_private_info import api_key,BOT_TOKEN,CHAT_ID

# _____________ OpenWeatherMap API Data _____________
api_link = "https://api.openweathermap.org/data/2.5/forecast"

latitude = 15.849695
longitude = 74.497673

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,  # Agle 12 ghanto ke 4 data points (har 3 ghante ka 1 slot)
}

response = requests.get(api_link, params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0])

bring_umbrella = False

for hour_data in weather_data["list"]:
  weather_id = hour_data["weather"][0]["id"]
  print(f"Forecast Weather Code: {weather_id}")

  # < 700 covers 2xx (Thunderstorm), 3xx (Drizzle), 5xx (Rain), 6xx (Snow)
  if int(weather_id) <= 500:
    bring_umbrella = True
    break

# _____________ Telegram Bot Setup _____________



# Message delivery test karne ke liye temporary: bring_umbrella = True

if bring_umbrella:
  message_text = "It's going to rain today. Please bring an umbrella ☂️"
  telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

  payload = {"chat_id": CHAT_ID, "text": message_text}

  tg_response = requests.post(telegram_url, json=payload)

  if tg_response.status_code == 200:
    print("Telegram Alert Sent Successfully!")
  else:
    print(f"Failed to send: {tg_response.text}")
else:
  print("No rain expected in the next 12 hours. No umbrella needed!")