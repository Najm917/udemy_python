import datetime as dt
import pandas as pd
import random,smtplib
from config import MY_EMAIL,MY_PASS

email=MY_EMAIL
password=MY_PASS

today=(dt.datetime.now())
today_tuple=(today.month,today.day)



date=pd.read_csv("birthdays.csv")


birtthday_dict={(date_raw["month"],date_raw["day"]): date_raw for (index,date_raw ) in date.iterrows()}

if today_tuple in birtthday_dict:
  birthday_person=birtthday_dict[today_tuple]
  file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
  
  with open(file_path) as letter_file:
    content=letter_file.read()
    content=content.replace("[NAME]", birthday_person["name"])
  
  with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
      from_addr=email,
      to_addrs=birthday_person["email"],
      msg = f"Subject: Happy Birthday!\n\n{content}"
    )


