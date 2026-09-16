

import random
from rock_paper import rock, paper, seissors

game_images = [rock, paper, seissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice < 0 or user_choice >= 3:
    print("You typed an invalid number, you lose!")
else:
    print("You chose:")
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    # Game comparison logic
    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose")