# Encapsulation example
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance


account = BankAccount("Aisha", 1000)
account.deposit(250)
account.withdraw(300)
print(account.get_balance())
