
from coffee_data import MENU, resources

profit = 0
is_on = True

DRINK_CHOICES = {
    "a": "espresso",
    "b": "latte",
    "c": "cappuccino",
    "d": "americano",
    "e": "flat_white",
    "f": "mocha",
}


def order_coffee(item_order, quantity):
    """Checks if enough resources exist for the total cups requested."""
    for key, amount in item_order.items():
        if amount * quantity > resources[key]:
            print(f"Sorry, there is not enough {key} for {quantity} cups.")
            return False
    return True


def process_money():
    """Calculates total money inserted."""
    print("\nPlease insert coins and notes:")
    total = int(input("How many ₹1 coins?: ") or 0) * 1
    total += int(input("How many ₹2 coins?: ") or 0) * 2
    total += int(input("How many ₹5 coins/notes?: ") or 0) * 5
    total += int(input("How many ₹10 coins/notes?: ") or 0) * 10
    total += int(input("How many ₹20 coins/notes?: ") or 0) * 20

    extra_cash = input("Do you have higher notes ('Y'/'N')?: ").strip().upper()
    if extra_cash == "Y":
        total += int(input("How many ₹50 notes?: ") or 0) * 50
        total += int(input("How many ₹100 notes?: ") or 0) * 100
        total += int(input("How many ₹200 notes?: ") or 0) * 200
        total += int(input("How many ₹500 notes?: ") or 0) * 500

    return total


def is_trsn_sucess(money_received, total_cost):
    """Verifies payment, adds to profit, and calculates return change."""
    global profit
    if money_received >= total_cost:
        remaning_amout = round(money_received - total_cost, 2)
        profit += total_cost
        if remaning_amout > 0:
            print(f"Here is your remaning amout ₹{remaning_amout}.")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded: ₹{money_received}")
        return False


def make_coffee(drink_name, order_ingredients, quantity):
    """Deducts ingredients for all cups and serves."""
    for item, amount in order_ingredients.items():
        resources[item] -= (amount * quantity)
    print(f"Here is your {quantity} cup(s) of {drink_name} ☕. Enjoy!\n")


while is_on:
    prompt = (
        "What would you like?\n"
        " 'A' for Espresso (₹150)\n"
        " 'B' for Latte (₹250)\n"
        " 'C' for Cappuccino (₹280)\n"
        " 'D' for Americano (₹180)\n"
        " 'E' for Flat White (₹260)\n"
        " 'F' for Mocha (₹290)\n"
        "Type choice (or 'report' / 'off'): "
    )
    choice = input(prompt).strip().lower()

    if choice == "off":
        is_on = False
        print("Machine shutting down...")

    elif choice == "report":
        print("\n--- Current Status ---")
        for key, value in resources.items():
            unit = "g" if key == "coffee" else "ml"
            print(f"{key.capitalize()}: {value}{unit}")
        print(f"Profit: ₹{profit}\n----------------------")

    elif choice in DRINK_CHOICES:
        drink_name = DRINK_CHOICES[choice]
        drink = MENU[drink_name]

        # 1. Ask quantity
        num_cups = int(input(f"How many cups of {drink_name.title()} do you want?: "))
        
        # 2. Check total resources needed
        if order_coffee(drink["ingredients"], num_cups):
            # 3. Calculate and display total amount
            total_cost = drink["cost"] * num_cups
            print(f"\nTotal bill for {num_cups} cup(s) of {drink_name.title()}: ₹{total_cost}")
            
            # 4. Process payment
            payment = process_money()
            if is_trsn_sucess(payment, total_cost):
                make_coffee(drink_name, drink["ingredients"], num_cups)
                is_on = False  # Turns machine off after serving
    else:
        print("Invalid selection. Please try again.\n")