from datetime import datetime, timedelta
import smtplib
import time
from config import MY_EMAIL, MY_PASS
import requests

# _______MY_Location (Belagavi)________
my_lat = 15.850154
my_long = 74.498042

# India IST offset (+5 ghante 30 minute)
IST_OFFSET = timedelta(hours=5, minutes=30)


# _____ISS Position API_______
def is_iss_overhead():
  try:
    iss_response = requests.get(
        "http://api.open-notify.org/iss-now.json", timeout=10
    )
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    print(f"ISS Position: Lat={iss_latitude}, Lng={iss_longitude}")

    if (my_lat - 5 <= iss_latitude <= my_lat + 5) and (
        my_long - 5 <= iss_longitude <= my_long + 5
    ):
      return True
    return False
  except Exception as e:
    print(f"ISS API Error: {e}")
    return False


# ________Sunrise Sunset API (Converted to IST +5:30)______
def is_night():
  try:
    parameters = {"lat": my_lat, "lng": my_long, "formatted": 0}
    sun_response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, timeout=10
    )
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    # UTC string ko datetime object me badalna
    utc_sunrise = datetime.fromisoformat(sun_data["results"]["sunrise"])
    utc_sunset = datetime.fromisoformat(sun_data["results"]["sunset"])

    # IST (+5:30) add karna
    ist_sunrise = utc_sunrise + IST_OFFSET
    ist_sunset = utc_sunset + IST_OFFSET

    # Indian Standard Time nikalna
    sunrise_hour = ist_sunrise.hour
    sunset_hour = ist_sunset.hour
    current_hour_ist = datetime.now().hour  # Local Indian time hour

    print(
        f"IST Now: {current_hour_ist}h | Sunset: {sunset_hour}h | Sunrise:"
        f" {sunrise_hour}h"
    )

    # Raat tab hoti hai jab sunset ke baad ho ya sunrise se pehle ho
    if current_hour_ist >= sunset_hour or current_hour_ist <= sunrise_hour:
      return True
    return False
  except Exception as e:
    print(f"Sunrise/Sunset Error: {e}")
    return False


# _____Main Loop_______
while True:
  time.sleep(5)

  iss_overhead = is_iss_overhead()
  night = is_night()

  print(f"Check -> Overhead: {iss_overhead} | Night: {night}")

  if iss_overhead and night:
    try:
      with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(
            to_addrs=MY_EMAIL,
            from_addr=MY_EMAIL,
            msg=(
                "Subject:Look Up 👆\n\nThe ISS is currently above you in the"
                " sky!"
            ),
        )
      print("Email sent successfully!")
    except Exception as e:
      print(f"Mail sending error: {e}")