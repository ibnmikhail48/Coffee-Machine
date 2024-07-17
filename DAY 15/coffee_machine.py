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

money_amount= 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(order_ingredients):
    """Returns true when order can be made, false if ingredients are insufficient"""
    for item in order_ingredients:
       if order_ingredients[item]>= resources[item]:
           print(f"Sorry there is not enough {item}.")
           return False
    return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
       change =round(money_received - drink_cost,2)
       print(f"here is ${change} in change")
       global money_amount
       money_amount += drink_cost
       return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def calculate_coins():
    """Returns the total calculated from coins insterted"""
    print("Please insert coins.")
    total= int(input("how many quarters? "))* 0.25
    total += int(input("how many dimes? "))* 0.1
    total += int(input("how many nickels? "))* 0.05
    total += int(input("how many pennies? "))* 0.01
    return total


def make_coffee(drink_name,order_ingredients):
    ### deduct the required in gredients from the resources##
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}🍵. Enjoy!")    

is_on =True
while is_on:
    coffee_choice=input("What would you like? (espresso/latte/cappuccino)")
    if coffee_choice == "off":
        is_on=False 
    elif coffee_choice == "report":
       print(f"water: {resources['water']}ml")
       print(f"Milk:{resources['milk']} ml")
       print(f"Coffee:{resources['coffee']}g")
       print(f" Money: ${money_amount}")
    else:
        drink_choice = MENU[coffee_choice]
        if is_resources_enough(drink_choice["ingredients"]):
            payment=calculate_coins()
            if is_transaction_successful(payment, drink_choice["cost"]):
                make_coffee(coffee_choice, drink_choice["ingredients"])
            
        

 