from coffee_data import resources as default_resources

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        # coffee_data.py se initial capacity lena
        self.resources = default_resources.copy()

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item, amount in drink.ingredients.items():
            if amount > self.resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item, amount in order.ingredients.items():
            self.resources[item] -= amount
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill(self):
        """Refills the resources back to full capacity."""
        self.resources = default_resources.copy()
        print("Machine resources have been successfully refilled!")