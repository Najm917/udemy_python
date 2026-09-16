print("welcome to ride this ride only for 120cm hight")
hight=int(input("plese enter your hight:\n"))
bill=0
if hight<=120:
  print("you can ride ")
  age=int(input("Enter your age\n"))
  if age <6:
    print("pay ₹20 for only ride ")
    bill=20
  elif age<12:
    print("pay ₹25 for only ride ")
    bill=25
  elif age<=20:
    print("pay ₹30 for only ride ")
    bill=30
  elif 45<=age<=55:
    print("ticket free")
    bill=0
  else:
    print("Sorry you can't ride because your age is over 20 years")
  picture_click=input("you want to click picture y or n if you want to click picture pay extra 15₹ :")   
  if picture_click.upper()=="Y":
    print(f"Final bill  ₹{bill+15} picture click and ride amount") 
  else:
    print(f"Final bill only ride amout ₹{bill}")
else:
  print("Sorry you can't ride because your height is over 120CM")