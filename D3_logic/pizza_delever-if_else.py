print("Welcomr to pizza deliveries!")
size=input("What's size of pizza you wants?. S/M/L/XL\n").strip().upper()

bill = 0

# 1. Base Pizza Price
if size == "S":
    bill += 149
elif size == "M":
    bill += 199
elif size == "L":
    bill += 249
elif size == "XL":
    bill += 349
else:
    print("Invalid size selected! Please restart.")
    # exit()

# pepproni section
pepproni = input("Do you want pepperoni on your pizza? Y or N\n").strip().upper()

if pepproni == "Y":
    types_of_peppronies = input("What size of pepperoni do you want? S / M (S size ₹40 and M size ₹60)\n").strip().upper()
    if types_of_peppronies == "S":
        bill += 40
    elif types_of_peppronies == "M":
        bill += 60
        
# cheese sction      
Extra_cheese=input("Do you want to extra cheese on your pizza? Y or N (cheese price is ₹80)\n").strip().upper()
if Extra_cheese=="Y":
  bill+=80


print("\n--- Order Summary ---")
print("Your pizza order is successfully placed!")
print("Please wait 20-25 minutes for delivery. Thank you!")
print(f"Total Amount to pay: ₹{bill}")       


