import random

letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','-','+']

print("Welcome to the PyPassword Generator!")
length_of_password=int(input("Length of password?\n"))
user_input_letter=int(input("How man letters would you havr in your password?\n"))
user_input_number=int(input("How many numbers in password?\n"))
user_input_symbol=int(input("How many symbols in password?\n"))

password=[]
for char in range(0,user_input_letter):
  password.append(random.choice(letter))
for char in range(0,user_input_number ):
  password.append(random.choice(numbers))
for char in range(0,user_input_symbol):
  password.append(random.choice(symbols))
  
random.shuffle(password)
print(f"Your password is: {''.join(password)}")