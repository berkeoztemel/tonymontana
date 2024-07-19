MENU = {
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


# TODO: 3. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def prompt_user():
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    return user_input

# TODO: 4. Turn off the Coffee Machine by entering “ off ” to the prompt.
# def shut_down(user_choice):
#        return exit
#
# # TODO: 5. Process coins.
def process_coins():
    print("Please insert coins")
    quarters = input("how many quarters?: ") # $0.25
    dimes = input("how many dimes?: ") # $0.10
    nickles = input("how many quarters?: ") # $0.05
    pennies = input("how many dimes?: ") # $0.01

    return quarters
    return dimes
    return nickles
    return pennies



# TODO: 6. Check transaction successful?


# TODO: 7. Make Coffee.
user_choice = prompt_user()


if user_choice == "report":
    report_message = report(user_choice)
    print(report_message)

if user_choice == "latte":
    process_coins()

print("last_Versioasadef")







