import random
from game_data import LIST_OF_INDIAN_FOLLOWERS
from art_logo import logo

score=0
is_continue=True
print("===== WELOCOME TO HIGH AND LOW GAME =====")

def name_generate(account):
  account_name=account["name"]
  account_profession=account["profession"]
  account_country=account["country"]

  return(f"{account_name}, a {account_profession} , from {account_country}")


def check_answer(user_guess,a_followers,b_followers):
  """ Take a user guess and  the followers count return"""
  if a_followers>b_followers:
    return user_guess=="A"
  else:
    return user_guess=="B"
  

account_b= random.choice(LIST_OF_INDIAN_FOLLOWERS)
while is_continue:
  # generate a  random account from  game data
  account_a=account_b
  account_b=random.choice(LIST_OF_INDIAN_FOLLOWERS)

  if account_a==account_b:
    account_b=random.choice(LIST_OF_INDIAN_FOLLOWERS)

  print(f"compare A : {name_generate(account_a)}")
  print(logo)
  print(f"Against B : {name_generate(account_b)}")

  guess= input("Who has more followers? 'A' or 'B': ").strip().upper()

  a_followers_count=account_a["followers_count"]
  b_followers_count=account_b["followers_count"]

  is_correct=check_answer(guess,a_followers_count,b_followers_count)
    

  if is_correct:
    score+=1
    print(f"you are right A:{a_followers_count}, B:{b_followers_count} ")
   
  else:
    
    print(f"thats wrong A:{a_followers_count}, B:{b_followers_count} ,Your  final score: {score}")
    is_continue=False
  
