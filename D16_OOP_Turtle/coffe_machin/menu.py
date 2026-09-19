from coffee_data import MENU

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks loaded from coffee_data."""
    def __init__(self):
        self.menu = []
        # coffee_data.py ke saare items load karna
        for item_name, details in MENU.items():
            ingredients = details.get("ingredients", {})
            self.menu.append(
                MenuItem(
                    name=item_name,
                    water=ingredients.get("water", 0),
                    milk=ingredients.get("milk", 0),
                    coffee=ingredients.get("coffee", 0),
                    cost=details.get("cost", 0)
                )
            )

    def get_items(self):
        """Returns all available drink names."""
        return "/".join([item.name for item in self.menu]) + "/"

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return None

