menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


# TODO: 1. Print report of all coffee machine resources

def report(user_choice):
    global resources
    if user_choice == "report":
        report_message = ""
        for resource, amount in resources.items():
            if resource != "coffee":
                unit = "ml"
            else:
                unit = "gr"
            report_message += f"{resource}: {amount}{unit}\n"
        return report_message


# TODO: 2. Check resources sufficient to make drink order
def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 3. Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    quarters = input("how many quarters?: ")  # $0.25
    dimes = input("how many dimes?: ")  # $0.10
    nickles = input("how many quarters?: ")  # $0.05
    pennies = input("how many dimes?: ")  # $0.01
    customer_amount = int(quarters) * 0.25 + int(dimes) * 0.10 + int(nickles) * 0.05 + int(pennies) * 0.01
    return customer_amount


# TODO: 4. Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

    # TODO: 5. Make Coffee.
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



is_on = True

while is_on:
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        report_message = report(choice)
        print(report_message)

    elif choice == "off":
        is_on = False

    else:
        drink = menu[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])




