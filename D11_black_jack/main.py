import random


CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}


def deal_card():
    cards = list(CARD_VALUES.keys())
    return random.choice(cards)


def calculate_score(cards):
    total = sum(CARD_VALUES[card] for card in cards)

    # Blackjack check
    if total == 21 and len(cards) == 2:
        return 0

    # Ace adjustment (agar 21 cross ho raha ho to Ace ko 1 maano)
    aces = cards.count("A")
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw! 🤝"
    elif comp_score == 0:
        return "You lose, Opponent has Blackjack! 💀"
    elif user_score == 0:
        return "Blackjack! You win! 🎉"
    elif user_score > 21:
        return "Your score 21 plus. You lose! 💥"
    elif comp_score > 21:
        return "Opponent's score 21 plus. You win! 🏆"
    elif user_score > comp_score:
        return "You win! 🏆"
    else:
        return "Opponent win. You lose! ❌"


# --- Game Start ---
print("=== WELCOME TO BLACKJACK ===")

user_cards = [deal_card(), deal_card()]
computer_cards = [deal_card(), deal_card()]

is_game_over = False

# --- Player's round ---
while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)

    print(f"\nYour cards: {user_cards} | Score: {user_score}")
    print(f"Computer's first card: ['{computer_cards[0]}']")

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else:
        choice = (
            input("Want to pick a new card press 'Y' otherwise press 'N': ")
            .strip()
            .lower()
        )
        if choice == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

# --- Computer's round ---
while comp_score != 0 and comp_score < 17 and user_score <= 21:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)

user_score = calculate_score(user_cards)


# --- Final Result ---
print("\n" + "=" * 30)
print(f"Your final hand: {user_cards} | Final Score: {user_score}")
print(f"Computer's final hand: {computer_cards} | Final Score: {comp_score}")
print(compare(user_score, comp_score))
print("\n" * 10)