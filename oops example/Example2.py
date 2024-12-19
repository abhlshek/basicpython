class bank:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance

    def __str__(self):
        return "name={0},account={1},balance={2}".format(self.name, self.balance, self.account)

    c = banks=("sushil", "106", "1000")
    print(c)
