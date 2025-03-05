# A dictionary that stores the menu items and their ingredients and cost
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 175,
    }
}
# The total profit made by the coffee machine
profit = 0

# A dictionary that stores the resources available in the coffee machine
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100
}


# A function that checks if the resources are available for the order
def check_resources(order_ingredients):
    """
    Checks if the resources are available for the order
    :param order_ingredients: A dictionary of ingredients and their quantities
    :return: A boolean indicating if the resources are available
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# A boolean that indicates if the coffee machine is on or off
is_on = True

while is_on:
    # Ask the user what they want
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # If the user wants to turn off the machine
    if choice == "off":
        is_on = False
    # If the user wants to print the report
    elif choice == "report":
        # Print the resources available
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        # Print the total profit made
        print(f"Money: Rs {profit}")
    else:
        # Get the coffee type from the menu
        coffee_type = Menu[choice]
        # Print the coffee type
        print(coffee_type)
        # Check if the resources are available
        if check_resources(coffee_type["ingredients"]):
            # Ask the user to insert the payment
            payment = int(input("Insert Rs "))
            # If the payment is enough
            if payment >= coffee_type["cost"]:
                # Calculate the change
                change = payment - coffee_type["cost"]
                # Print the change
                print(f"Here is your change Rs {change}")
                # Add the profit to the total profit
                profit += coffee_type["cost"]
                # Reduce the resources available
                for item in coffee_type["ingredients"]:
                    resources[item] -= coffee_type["ingredients"][item]
                # Print a message indicating that the coffee is ready
                print(f"Here is your {choice} . Enjoy!")
            else:
                # Print a message indicating that the payment is not enough
                print("Sorry that's not enough money. Money refunded.")
        else:
            # Print a message indicating that the resources are not available
            print("Sorry, we don't have enough resources.")

