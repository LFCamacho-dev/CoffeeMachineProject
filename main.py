# Main script
import payment

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
    "water": 200,
    "milk": 200,
    "coffee": 100,
}

money = 0
can_make_drink = False


def placing_order():
    print(resources)
    input_order = input(f"Welcome to Cafe Python! "
                        f"What would you like? (espresso($1.5) / latte($2.5) / cappuccino ($3.0):").lower()

    if input_order == "off":
        print("Shutting down...")
        quit()
    elif input_order == "report":
        print_report()
        placing_order()
    elif input_order == "espresso" or input_order == "latte" or input_order == "cappuccino":
        print(f"Your ordered: {input_order}")
        check_resources(input_order)
        if can_make_drink: payment.make_payment(input_order)
    else:
        print("Wrong order, please try again")
        placing_order()


def print_report():
    print(f"""
    Water: {str(resources.get("water"))}ml
    Milk: {str(resources.get("milk"))}ml
    Coffee: {str(resources.get("coffee"))}g
    Money: ${money}
""")


def check_resources(input_order):
    water_needed = MENU.get(input_order, {}).get("ingredients").get("water")
    milk_needed = MENU.get(input_order, {}).get("ingredients").get("milk")
    coffee_needed = MENU.get(input_order, {}).get("ingredients").get("coffee")
    # bevy_cost = MENU.get(input_order, {}).get("cost")
    water_available = resources.get("water")
    milk_available = resources.get("milk")
    coffee_available = resources.get("coffee")

    if not water_needed <= water_available:
        print("Sorry, there is not enough water")
        placing_order()

    elif not coffee_needed <= coffee_available:
        print("Sorry, there is not enough coffee")
        placing_order()

    elif input_order != "espresso":
        if not milk_needed <= milk_available:
            print("Sorry, there is not enough milk")
            placing_order()

    # defining globals
    global can_make_drink
    can_make_drink = True

    return water_needed


if __name__ == "__main__":
    placing_order()

