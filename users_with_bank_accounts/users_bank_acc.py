class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        if amount <= 0:
            raise Exception ("The deposit has to be above $0.")
        return self
        

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0 :
            raise Exception (f'Insufficient funds: Charging a $5 fee. Now your balance is: $ {self.balance - 5 } Please contact the bank ASAP!')
        return self

class User:

    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.account_type = account_type
        self.account = BankAccount(int_rate = 0.02, balance = 0)
        print(f'{self.name} {self.account_type} balance is $ {self.account.balance}')
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.name, "deposit $", amount, "into", self.account_type, "account")
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(self.name, "withdraw $", amount, "from", self.account_type, "account")
        return self
    
    def display_user_balance(self):
        print(f'{self.name} {self.account_type} balance is $ {self.account.balance}')
        return self

    def transfer(self, activity, amount):
        if activity == "sending":
            self.account.withdraw (amount)
            print(self.name, "is transfering $", amount, "to Savings account")
        elif activity == "receiving":
            self.account.deposit (amount)
            print(self.name, "received $", amount, "from Checking account")
        return self




    def yield_interest(self):
        print(f'Your {self.account_type} interest rate is: $ {self.account.int_rate}')
        if self.account.balance > 0:
            self.account.balance += self.account.balance * self.account.int_rate
            print("Congratulations! Your interest rate is on the way. Your", self.account_type, "balance is now $ " + str(self.account.balance))
        else:
            print("There is no interest rate at the moment. Please contact the bank for any further information.")
        return self


checking = User('Sabrina Sams', "SabrinaSams@gmail.com", "Checking")
saving = User('Sabrina Sams', "SabrinaSams@gmail.com", "Savings")

try:

    saving.make_deposit(500)
    checking.make_deposit(1200)
    checking.make_deposit(1500)
    checking.make_withdraw(300)
    checking.display_user_balance()
    checking.transfer("sending", 1000)
    saving.transfer("receiving", 1000)
    checking.display_user_balance()
    checking.yield_interest()
    saving.display_user_balance()
    saving.yield_interest()

except Exception as a:
    print(a)
