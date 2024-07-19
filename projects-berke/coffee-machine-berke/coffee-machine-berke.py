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

bank_account_amount = 0


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


# TODO: 2. Check resources sufficient to make drink order

def resources_sufficient():
    ''' every order refresh the resources '''
    if status == True:
        remaining_water = resources["water"] - menu[user_choice]["ingredients"]["water"]
        return remaining_water





# TODO: 3. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def prompt_user():
    ''' Ask customer about what would you like to drink?(espresso/latte/cappucino) '''
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    return user_input


# TODO: 4. Turn off the Coffee Machine by entering “ off ” to the prompt.
def shut_down():
    '''Shutdown the coffee machine '''
    return exit()

# TODO: 5. Process coins.
def process_coins():
    ''' Calculate the total amount of customer money '''
    print("Please insert coins")
    quarters = input("how many quarters?: ")  # $0.25
    dimes = input("how many dimes?: ")  # $0.10
    nickles = input("how many quarters?: ")  # $0.05
    pennies = input("how many dimes?: ")  # $0.01
    total_amount = int(quarters) * 0.25 + int(dimes) * 0.10 + int(nickles) * 0.05 + int(pennies) * 0.01
    return total_amount


# TODO: 6. Check transaction successful?

def transaction_check():
    ''' Check the transaction. Is there any enough money or no '''
    global bank_account_amount
    if customer_amount > (menu[user_choice]["cost"]):
        change_left = round(customer_amount - (menu[user_choice]["cost"]),2)
        bank_account_amount += (menu[user_choice]["cost"])

        return True, f"Here is ${change_left} in change"
    else:
        return False, "Sorry that's not enough money. Money refunded."


# TODO: 7. Make Coffee.

while True:
    user_choice = prompt_user()
    if user_choice == "report":
        report_message = report(user_choice)
        print(report_message)

    if user_choice == "latte":
        customer_amount = process_coins()
        status, message = transaction_check()
        print(message)
        print(f"Here is your {user_choice}. Enjoy!")


