class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        if amount <= 0:
            raise Exception ("The deposit has to be above $0.")
        print("You deposit: $", amount)
        print(f'Your balance is: $ {self.balance}')
        return self
        

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance <= 0 :
            raise Exception (f'Insufficient funds: Charging a $5 fee. Now your balance is: $ {self.balance - 5 } Please contact the bank ASAP!')
        print("You withdraw: $", amount)
        print(f'Your balance is: $ {self.balance}')
        return self


    def display_account_info(self): 
        print(f'You balance is: $ {self.balance}')
        print(f'The interest rate is: $ {self.int_rate}')
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            print("Congratulations! Your interest rate is on the way. Your balance is now: $ " + str(self.balance))
        else:
            print("There is no interest rate at the moment. Please contact the bank for any further information.")
        return self

        

mr_a = BankAccount(0.01, 1000)
mr_b = BankAccount(0.01, 500)

try:

    mr_a.deposit(500).deposit(200).deposit(100).withdraw(300).display_account_info().yield_interest()

    mr_b.deposit(400).deposit(100).withdraw(500).withdraw(400).withdraw(100).withdraw(100).display_account_info().yield_interest()

except Exception as a:
    print(a)

