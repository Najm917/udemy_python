import datetime as dt
import random
import smtplib
from config import MY_EMAIL,MY_PASS

my_email=MY_EMAIL
my_password=MY_PASS



now = dt.datetime.now()
weekday = now.weekday()  # Monday = 0, tuesday=1 etc

if weekday == 2:
    with open("quots.txt", "r", encoding="utf-8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes).strip()
    
    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        # sendmail must be inside the connection context block
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: {weekday} Motivation\n\n{quote}"
        )
    
    print("Email sent successfully")