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
def checking_stock(coffee_type):
    if(resources['water'] < MENU[coffee_type]['ingredients']['water'] or resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']):
        print("There are no sufficient materials to make the requested coffe")
        coffee_machine()
    elif (resources['water'] < MENU[coffee_type]['ingredients']['water'] or resources['milk'] < MENU[coffee_type]['ingredients']['milk']  or resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']):
        print("There are no sufficient materials to make the requested coffe")
        coffee_machine()
    else:
        resources['water']  = resources['water'] - MENU[coffee_type]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']

def espresso_stock(coffee_type):
    if (resources['water'] < MENU[coffee_type]['ingredients']['water'] or resources['coffee'] < MENU[coffee_type]['ingredients']['coffee']):
        print("There are no sufficient materials to make the requested coffe")
        coffee_machine()
    else:
        resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']

def money_validation(coffee_type):
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How may nickles'))
    penny = int(input('How many penny'))
    user_given_amount = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (penny*0.01)
    if (user_given_amount == MENU[coffee_type]['cost']):
        print(f"Here is your {coffe_type}...!")
    elif (user_given_amount > MENU[coffee_type]['cost']):
        change = user_given_amount - MENU[coffee_type]['cost']
        print(f"Your Change is {change} !")
        print(f"Here is your {coffee_type}...!")
    else:
        print("Sorry ! Money is inusfficient")

def coffee_machine():
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    if (coffee_type == 'off'):
        print("Turning Off Coffee Machine...!")
        exit()
    elif ( coffee_type == 'report'):
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        coffee_machine()
    elif ( coffee_type == 'espresso'):
        espresso_stock(coffee_type)
        money_validation(coffee_type)
        coffee_machine()
    elif( coffee_type == 'latte'):
        checking_stock(coffee_type)
        money_validation(coffee_type)
        coffee_machine()
    elif(coffee_type == 'cappuccino'):
        checking_stock(coffee_type)
        money_validation(coffee_type)
        coffee_machine()
coffee_machine()
