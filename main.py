MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(choice):
    """Compares resources stored to user's order."""
    water_left = resources["water"]
    milk_left = resources["milk"]
    coffee_left = resources["coffee"]

    water_needed = MENU[choice]["ingredients"]["water"]
    milk_needed = MENU[choice]["ingredients"]["milk"]
    coffee_needed = MENU[choice]["ingredients"]["coffee"]

    if water_left < water_needed:
        print("Sorry there is not enough water.")
        return False
    elif milk_left < milk_needed:
        print("Sorry there is not enough milk.")
        return False
    elif coffee_left < coffee_needed:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def make_coffee(choice, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


def check_currency(q, d, n, p, choice):
    """Compares the cost of drink to money inserted."""
    quart_total = q * .25
    dime_total = d * .10
    nick_total = n * .05
    pen_total = p * .01
    coins_total = quart_total + dime_total + nick_total + pen_total
    coffee_cost = MENU[choice]["cost"]

    if coffee_cost > coins_total:
        print("“Sorry that's not enough money. Money refunded.")
        return False
    else:
        total_cost = round(coins_total - coffee_cost, 2)
        print(f"Here is ${total_cost} in change.")
        global profit
        profit += coffee_cost
        return True


def resource_report(choice):
    """Prints resources and money in machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def coffee_machine():
    continue_drinks = True

    while continue_drinks:
        user_choice = input("   What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            continue_drinks = False
        elif user_choice == "report":
            resource_report(user_choice)
        else:
            if check_resources(user_choice):
                print("Please insert coins.")
                quarters = float(input("How many quarters? "))
                dimes = float(input("How many dimes? "))
                nickles = float(input("How many nickles? "))
                pennies = float(input("How many pennies? "))
                if check_currency(quarters, dimes, nickles, pennies, user_choice):
                    make_coffee(user_choice, MENU[user_choice]["ingredients"])


coffee_machine()
