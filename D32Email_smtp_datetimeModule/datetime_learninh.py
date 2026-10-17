import datetime as dt
now=dt.datetime.now()
day=now.day

# print(now)
# print(day)
y=int(input("enter year: "))
month=int(input("enter month: "))
day=int(input("enter day: "))

dob=dt.datetime(year=y,month=month,day=day)
print(dob)