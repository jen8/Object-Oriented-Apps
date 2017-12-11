class BankAccount:
    def __init__(self, account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        self.amount -= withdraw_amount

    def __str__(self):
        return "{} Amount: {}".format(self.account_type, self.amount)

stephanie = BankAccount("Checkings", 100)
print(stephanie.account_type)
print(stephanie.amount)

stephanie.deposit(30)
print(stephanie.amount)

stephanie.withdraw(45)
print(stephanie.amount)

print(stephanie) # after adding __str__ method we will see str rep instead of object

