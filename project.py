# For this assignment, don't worry about 
# putting any user information in the BankAccount class. 

# Let's first just get some more practice writing classes
#  by writing a new BankAccount class. In the next lesson,
#  we'll tie our User and BankAccount classes together.

# The BankAccount class should have a balance. When a new
#  BankAccount instance is created, if an amount is given,
#  the balance of the account should initially be set to
#  that amount; otherwise, the balance should start at $0.
#  The account should also have an interest rate, saved as
#  a decimal (i.e. 1% would be saved as 0.01), which should
#  be provided upon instantiation. (Hint: when using default
#  values in parameters, the order of parameters matters!)

# 1. Create a BankAccount class with the attributes interest rate and balance

# 2. Add a deposit method to the BankAccount class

# 3. Add a withdraw method to the BankAccount class

# 4. Add a display_account_info method to the BankAccount class

# 5. Add a yield_interest method to the BankAccount class

# 6. Create 2 accounts

# 7. To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)

# 8. To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)



class User:
    def __init__(self, name, account):
        self.name = name


class BankAccount:
    def __init__(self, balance=0, interest=0.01):
        self.balance = balance
        self.interest = interest

    def deposit(self, amount):           #increases the account balance by the given amount
        self.balance += amount
        return self

    def withdraw(self, amount):           #decreases the account balance by the given amount or prints a message and deduct $5
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):             #print to the console: eg. "Balance: $100"
        print(f"Balance: ${self.balance}")

    def yield_interest(self):           #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.interest *self.balance 
        return self


alpha = BankAccount()
alpha.deposit(50).deposit(50).deposit(50).withdraw(14).yield_interest()
alpha.display_account_info()

beta = BankAccount(20, 0.05)
beta.deposit(50).deposit(59).withdraw(5).withdraw(1).withdraw(4).withdraw(1).yield_interest()
beta.display_account_info()
