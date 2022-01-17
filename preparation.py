# Module with preparation steps
import main


def preparing_drink(drink):
    print(f"I'm preparing your {drink}, hold on...")

    water_needed = main.MENU.get(drink, {}).get("ingredients").get("water")
    milk_needed = main.MENU.get(drink, {}).get("ingredients").get("milk")
    coffee_needed = main.MENU.get(drink, {}).get("ingredients").get("coffee")

    # adjust available ingredients
    main.resources["water"] -= water_needed
    main.resources["coffee"] -= coffee_needed
    if not drink == "espresso": main.resources["milk"] -= milk_needed

    print(f"Here's your {drink}, Enjoy!")

    main.placing_order()
