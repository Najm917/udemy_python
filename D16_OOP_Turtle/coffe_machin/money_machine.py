class MoneyMachine:

    CURRENCY = "₹"

    DENOMINATIONS = {
        "₹5 notes/coins": 5,
        "₹10 notes/coins": 10,
        "₹20 notes/coins": 20,
        "₹50 notes": 50,
        "₹100 notes": 100,
        "₹200 notes": 200,
        "₹500 notes": 500
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Accepts notes/coins from user and returns total."""
        print("Please insert money (notes/coins).")
        for note, value in self.DENOMINATIONS.items():
            count = input(f"How many {note}?: ").strip()
            if count.isdigit():
                self.money_received += int(count) * value
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            if change > 0:
                print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry that's not enough money. Received {self.CURRENCY}{self.money_received}, but cost is {self.CURRENCY}{cost}. Money refunded.")
            self.money_received = 0
            return False
        
        
        