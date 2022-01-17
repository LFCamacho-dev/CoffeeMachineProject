import main

penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25


def make_payment(drink):
    quarters_received = input("Please insert Quarters ($0.25): ")
    dimes_received = input("Please insert Dimes ($0.10): ")
    nickels_received = input("Please insert Nickels ($0.05): ")
    pennies_received = input("Please insert Pennies ($0.01): ")

    money_received = (float(quarters_received) * quarter) + \
                     (float(dimes_received) * dime) + \
                     (float(nickels_received) * nickel) + \
                     (float(pennies_received) * penny)

    print(f"Money received: ${money_received}")
    print(f"The cost of your drink is: $ {main.MENU.get(drink, {}).get('cost')}")

    if money_received >= main.MENU.get(drink, {}).get("cost"):
        print("making order!")  # TODO Finish the order, calculate change and create script for making order :)
    else:
        print("Sorry that's not enough money. Money refunded.")
        main.placing_order()
