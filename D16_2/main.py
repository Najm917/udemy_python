from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machin=MoneyMachine()
coffe_maker=CoffeeMaker()
menu=Menu()





is_on=True
while is_on:
  option=menu.get_items()
  choice = input(f"What would you like? ({option}) [type 'report' or 'off']: ").lower()
  if choice =="off":
    is_on=False
  elif choice=="report":
    money_machin.report()
  else:
    drink=menu.find_drink(choice)
    print(f"Cost of {drink.name.title()}: {money_machin.CURRENCY}{drink.cost}")
    if coffe_maker.is_resource_sufficient(drink):
      if money_machin.make_payment(drink.cost):
        coffe_maker.make_coffee(drink)
        is_on=False
    

