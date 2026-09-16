import random
from random import randint

def check_answer(user_guess,actule_guess):
  if user_guess>actule_guess:
    return "To higt!"
  elif user_guess<actule_guess:
    return "To low"
  else:
    return "Right answer!"
  

system_generate=random.randint(1,100)
# print(system_generate)
while True:
    
  guess=int(input("enter a number: "))
  

  answer=check_answer(guess,system_generate)
  print(answer)
  
  
  if guess==system_generate:
    break
  