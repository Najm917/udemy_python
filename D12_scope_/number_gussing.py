from random import randint
EASY_TURNS = 10
HARD_TURNS = 5

game_continue=True

def check_answer(user_guess,actule_guess,turn):
  if user_guess>actule_guess:
    print("To Hight!")
    return turn-1
  elif user_guess<actule_guess:
    print("To Low! ")
    return turn-1
    
    
    
  else:
    print(f"cogratulation your guess {user_guess} perfect match to actule guess: {actule_guess}")
    return turn

def set_dificulty():
  while game_continue:
    choose_dificulty=input("choose dificulty 'easy' or 'hard'?: ").lower()
    if choose_dificulty=="easy":
      return EASY_TURNS
      
      
    elif choose_dificulty=="hard":
      return HARD_TURNS
      
    else:
      print("Invalid choice. Please enter 'easy' or 'hard'.")

def game():
  print("====WELCOME TO NUMBER GUESSING GAME====")
  print("I an thinking to a number between 1 to 100")
  answer=randint(1,100)



  turn=set_dificulty()
  
  guess = 0
  while guess != answer:
        print(f"You have {turn} attempts remaining.")
        try:
            guess = int(input("Guess a number from 1 to 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        turn=check_answer(guess, answer, turn)

        if guess == answer:
            break
        elif turn <= 0:
            print(f"You've run out of guesses. The correct answer was {answer}. You lose!")
            break
while game_continue:
    game()
    restart = input(
        "\nWant to restart the game? (1 for Yes, 0 for No): "
    ).strip()
    if restart != "1":
        print("Thanks for playing! Goodbye.")
        game_continue = False

