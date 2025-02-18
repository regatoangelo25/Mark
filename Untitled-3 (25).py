# Task 3: BankAccount class with account_number, owner, and balance attributes

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account balance: {self.balance}")

# Create an account and perform transactions
account = BankAccount("12345", "John Doe", 500)
account.deposit(200)
account.withdraw(100)
account.display_balance()