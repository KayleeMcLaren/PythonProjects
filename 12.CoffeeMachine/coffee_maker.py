class CoffeeMaker:
    # Models the machine that makes the coffee
    # The __init__() method is the constructor for the CoffeeMaker class.
    # It initializes the resources attribute, which is a dictionary that stores the current
    # levels of water, milk, and coffee in the machine
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        # Prints a report of all resources
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    # is_resource_sufficient() method checks if the coffee machine has enough resources to make the specified drink
    def is_resource_sufficient(self, drink):
        # Returns True when order can be made, False if ingredients are insufficient
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    # make_coffee() method makes the specified drink by deducting the required ingredients from the resources
    # It then prints a message to the user indicating that the drink is ready
    def make_coffee(self, order):
        # Deducts the required ingredients from the resources
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
