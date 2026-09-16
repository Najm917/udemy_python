from random import randint
print("==== WELCOME TO NUMBER GUESSING GAME ====")
game_continue=True
LIFE=0
level=input("Dificulty level easy 10 chance and hard 5: 'easy' or ''hard': ").lower()

def check_ans(user_guess,actule_ans):
  global LIFE
  if user_guess>actule_ans:
    print("To hight!")
    LIFE-=1
    
  elif user_guess<actule_ans:
    print("To low!")
    LIFE-=1
  else:
    print("correct guess")
    LIFE+=1

def check_dificulty():
  global LIFE
  while game_continue:
    
    if level=="easy":
      LIFE =10
      break
    elif level=='hard':
      LIFE=5
      break
    else:
      print("Invalid choice. Please enter 'easy' or 'hard' .")
      
      break


def game():
  global LIFE
  print("I am thinking between 1 to 100")
  answer=randint(1,100)
  
  check_dificulty()
  guess=0
  while game_continue:
    print(f"remaning life: {LIFE}")
    
    try:
      guess=int(input("guess number 1 to 100: "))
    except ValueError:
      print("please enter a valid number. ")
      continue
    check_ans(guess,answer)
    
    if LIFE<=0:
      print(f"game over life remaning: {LIFE}")
      break
    
game()
  
