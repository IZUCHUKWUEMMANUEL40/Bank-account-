class Account:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return "Withdrawal successful"

class Savings(Account):
    def __init__(self):
        super().__init__()

    def withdraw(self, amount):
        if amount > 5000:
            return "You have reached your daily limit"
        else:
            return super().withdraw(amount)

savings = Savings()
print(savings.withdraw(2000))
