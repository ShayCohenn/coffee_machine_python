from data import COINS, resources, MENU

def report():
    """returns None - prints the remaining resources"""
    print(f"Resources: {resources}")

def buy_coffee(coffee_name):
    """returns change: float - returns the change in the cost of the coffee."""
    total_money = 0
    for coin in COINS:
        money = input(f"How many {coin}s? ")
        if not money.isdigit():
            print("Please enter a number.")
            buy_coffee(coffee_name)
        total_money += int(money) * COINS[coin] / 100
    change = round(total_money - MENU[coffee_name]['cost'], 2)
    return change

def check_resources(coffee_name):
    """returns True | False - returns True if the resources are sufficient, False otherwise."""
    for ing in MENU[coffee_name]['ingredients']:
        if resources[ing] < MENU[coffee_name]['ingredients'][ing]:
            print(f"Sorry, we don't have enough {ing}.")
            return False
    return True

def remove_resources(coffee_name):
    """returns None - removes the resources from the resources"""
    for ing in MENU[coffee_name]['ingredients']:
        resources[ing] -= MENU[coffee_name]['ingredients'][ing]

def main(coffee_choice):
        """returns None - main function that makes the coffee."""
        change = buy_coffee(coffee_choice)
        if change > 0:
            print(f"Here is ${change} in change.")
        elif change == 0:
            print(f"No change needed you paid the exact amount.")
        else:
            print(f"Sorry, you don't have enough money. You're missing {-change}")
            return
        remove_resources(coffee_choice)
        print(f"Here is your {coffee_choice}. Enjoy! ☕")

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == 'off':
        break
    elif user_input == 'report':
        report()
    elif user_input not in MENU:
        print("Please enter a valid choice.")
    else:
        print(f"You chose {user_input} ")
        if check_resources(user_input):
            print(f"That will be ${MENU[user_input]['cost']}")
            if input("Type (confirm) to confirm your order or type (cancel) to cancel the order: ").lower() == "confirm":
                main(user_input)