from datetime import datetime, timezone
import smtplib
import time
from config import MY_EMAIL, MY_PASS
import requests
# _______MY_Location________
my_lat=15.850154
my_long=74.498042



# _____iss position api_______
def is_iss_overhead():
  iss_response = requests.get("http://api.open-notify.org/iss-now.json")
  iss_response.raise_for_status()
  iss_data = iss_response.json()

  iss_latitude = float(iss_data["iss_position"]["latitude"])
  iss_longitude = float(iss_data["iss_position"]["longitude"])

  if (my_lat-5<=iss_latitude <=my_lat+5) and (my_long-5 <= iss_longitude<= my_long+5):
    return True
  return False

#________sunrice sunset api______
def is_night():
  parameters={
    "lat": my_lat,
    "lng": my_long,
    "formatted":0
  }
  sun_response = requests.get(
      "https://api.sunrise-sunset.org/json", params=parameters
  )
  sun_response.raise_for_status()
  sun_data = sun_response.json()

  sunrise=sun_data["results"]["sunrise"]
  sunset=sun_data["results"]["sunset"]


  sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
  sunset_hour = int(sunset.split("T")[1].split(":")[0])

  time_now = datetime.now(timezone.utc).hour
  if  time_now >= sunset_hour or time_now <= sunrise_hour: 
    return True
  return False
    
while True:
  time.sleep(2)
  if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
      connection.starttls()
      connection.login(user=MY_EMAIL,password=MY_PASS)
      connection.sendmail(to_addrs=MY_EMAIL,from_addr=MY_EMAIL,msg="Subject:look Up\n\nThe ISS currently above you in the sky!")
  print("Email sent ")

