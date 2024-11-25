class Union:
    def __init__(self, accountno, name, balance):
        self.accountno = accountno
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return "account no: {0}, name: {1}, balance: {2}".format(self.accountno, self.name, self.balance)


bank = Union(101, "Popat Lal", 1000)
print(bank)
bank.deposit(10000)
print(bank)
bank.withdraw(2000)
print(bank)
