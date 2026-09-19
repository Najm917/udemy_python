from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"\nWhat would you like? ({options}): ").strip().lower()

    if choice == "off":
        is_on = False
        print("Turning off coffee machine. Goodbye!")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "refill":
        coffee_maker.refill()
    else:
        drink = menu.find_drink(choice)
        if drink:
            print(f"Cost of {drink.name.title()}: {money_machine.CURRENCY}{drink.cost}")
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    
<<<<<<< HEAD
                    
                    
=======
                
>>>>>>> 3149dfaf0d4462ca88487e0e7c2749ff44e97704
