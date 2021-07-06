class user:
    def __init__(self, name):
        self.name = name
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def balance(self):
        print(self.name)
        print(self.accountBalance)
        return self

    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount
        otherUser.accountBalance += amount
        return self


logan = user("logan")
jacob = user("jacob")
william = user("william")

logan.makeDeposit(200).makeDeposit(50).makeDeposit(1000).makeWithdrawal(350)
print(logan.accountBalance)

jacob.makeDeposit(7).makeDeposit(3).makeWithdrawal(5).makeWithdrawal(4)
print(jacob.accountBalance)

william.makeDeposit(1000).makeWithdrawal(
    250).makeWithdrawal(450).makeWithdrawal(50)
print(william.accountBalance)

logan.transferMoney(william, 300)
print(logan.accountBalance)
print(william.accountBalance)
