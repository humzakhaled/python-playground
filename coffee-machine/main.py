from menu import MENU, art, resources

def print_header():
    print(art)
    print("=" * 30)

def get_user_choice():
    print("\nWhat would you like?")
    print("- espresso")
    print("- latte")
    print("- cappuccino")
    print("- report (check inventory)")
    print("- off (shut down)")

    while True:
        choice = input('\nSelection: ').strip().lower()
        if choice in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
            return choice
        print('Invalid input. Please try again.')


def report():
    print("\n--- Current Resources ---")
    for item, quantity in resources.items():
        unit = "ml" if item != "coffee" else "g"
        print(f"{item.capitalize():<8}: {quantity}{unit}")
    print("-------------------------\n")


def calculate_total(quarters, dimes, nickels, pennies):
    return round((quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01), 2)

def get_float(money):
    while True:
        try:
            return float(input(f"Enter {money}: "))
        except ValueError:
            print("Please enter a valid number.")

def check_resources(selection):
    for item, amount in MENU[selection]['ingredients'].items():
        if resources[item] < amount:
            print(f"\n[!] Sorry, not enough {item} available to make {selection}.")
            return False
    return True

def use_resources(selection):
    for item, amount in MENU[selection]['ingredients'].items():
        resources[item] -= amount

def make_coffee(selection):
    if not check_resources(selection):
        return

    cost = MENU[selection]['cost']
    print(f"\nThat will be ${cost:.2f}.")
    print("Please insert coins:")
    
    quarters = get_float('quarters')
    dimes = get_float('dimes')
    nickels = get_float('nickels')
    pennies = get_float('pennies')
    
    total = calculate_total(quarters, dimes, nickels, pennies)

    if total < cost:
        print("\n[!] Not enough money. Refunding coins.")
    else:
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        
        use_resources(selection)
        print(f"Here is your {selection.upper()}! ☕ Enjoy!")

def coffee_maker():
    print_header()
    while True:
        selection = get_user_choice()
        
        if selection == 'off':
            print("\nShutting down. Goodbye!")
            break 
        elif selection == 'report':
            report()
        else:
            make_coffee(selection)

coffee_maker()