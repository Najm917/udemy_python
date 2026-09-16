import random
import words_list
life=3
restart=True
while restart:
  
#  choosing a random word from the list of words
  random_words=words_list.random_words_list
  print(f"The list of words: {random_words}")

  system_guess=random.choice(random_words)
  

  # placeholder same as the number of words
  print("_ "*len(system_guess))


  # user guess section
  game_over=False
  guess_letter=[]
  while not game_over:
    user_guess=input("Guess a letter whose word it is: ").lower()

# Avoiding duplicate letters and life not increasing for duplicate letters
    if user_guess in guess_letter:
      print(f"You already guessed {user_guess}. Try again.")
      continue
# life decreasing and increasing based on the user guess
    disply=""
    if user_guess not in system_guess:
      life-=1
      print(f"Wrong guess remaning:   {life}")
    else:      
      life+=1
      print(f"Right guess +1 remaning: {life}")
    if life<=0:
      game_over=True
      print(f"Game over! You lose remaning: {life}.")
      continue
# Display the current state of the word
    for letter in system_guess:
      if letter==user_guess:
      
        disply+=letter
        guess_letter.append(user_guess)
      elif letter in guess_letter:
        disply+=letter
      else:
        disply+="_ "
    print(disply)
    if "_ " not in disply:
      game_over =True
      print("you win")
# Ask if the player wants to play again
  again=input("Continue game Y for yes and N for no: ").strip().upper()
  life_reset=3
  if life==0:
    life=life_reset 
  else:
    life==life
    
  if again=="Y":
    restart=True
  else:
    restart=False
      
    
