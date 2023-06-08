
all_accounts = {"Banana Bee": 500, "Papaya Pee": 1000}

def get_balance():
    print("Your balance is:", all_accounts)

def deposit(amount):
    if amount <= 0:
        raise Exception ("The deposit has to be above $0.")
    print("Your deposit is: $", amount)
    all_accounts["Banana Bee"] += amount

def withdraw(amount):
    if amount > all_accounts["Banana Bee"]:
        raise Exception ("You don't have enough money to withdraw.")
    print("Your withdraw is: $", amount)
    all_accounts["Banana Bee"] -= amount

try:
    get_balance()
    deposit(500)
    get_balance()
    deposit(200)
    get_balance()
    deposit(100)
    get_balance()
    withdraw(300)
    get_balance()
except Exception as a:
    print(a)

