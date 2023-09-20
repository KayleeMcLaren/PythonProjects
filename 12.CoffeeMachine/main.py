from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates instances of the MoneyMachine, CoffeeMaker, and Menu classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Declares a variable called is_on and sets it to True - used to control the loop that runs the coffee machine
is_on = True

# Starts a loop that will continue to run as long as the is_on variable is set to True
while is_on:
    # Gets the list of available menu items from the Menu object and prompts the user to choose an item
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    # If the user chooses the "off" option, the is_on variable is set to False and the loop exits
    if choice == "off":
        is_on = False
    # If the user chooses the "report" option, the CoffeeMaker and MoneyMachine objects are called to generate reports on their current status
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Otherwise, the user's choice is used to find the corresponding Drink object from the Menu object
    else:
        drink = menu.find_drink(choice)
        # If the CoffeeMaker has enough resources to make the drink and the MoneyMachine accepts the payment, the CoffeeMaker makes the drink
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
