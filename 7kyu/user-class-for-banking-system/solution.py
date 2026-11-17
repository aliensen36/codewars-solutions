class User:

    def __init__(self, name: str, balance: int, checking_account: bool):
        # the account holder's name
        self.name = name
        # the initial balance
        self.balance = balance
        # whether this user can issue checks to others
        self.checking_account = checking_account

    def withdraw(self, amount):
        """Withdraw `amount` from this account, if balance is sufficient"""
        if self.balance < amount:
            raise ValueError(f"Overdraw! {self.name} has only {self.balance}.")
        self.balance -= amount
        return f"{self.name} has {self.balance}."

    def add_cash(self, amount):
        """Deposit `amount` into this account"""
        self.balance = int(self.balance + amount)
        return f"{self.name} has {self.balance}."

    def check(self, issuer, amount):
        """Receive a check from `issuer` over `amount`, if possible

        `issuer` is the User issuing the check, i.e. the account the `amount` will be taken from
        `self` is the User receiving the check, i.e. the account the `amount` will be added to
        """
        if issuer.checking_account is False:
            raise ValueError(f"{issuer.name} is not a checking account.")
        if amount > issuer.balance:
            raise ValueError(f"{issuer.name} has only {issuer.balance}.")
        issuer.balance -= amount
        self.balance += amount
        return f"{self.name} has {self.balance} and {issuer.name} has {issuer.balance}."


Jeff = User('Jeff', 70, True)
Joe  = User('Joe',  70, False)

print(Jeff.withdraw(2))    # 'Jeff has 68.'
print(Joe.check(Jeff, 50))    # 'Joe has 120 and Jeff has 18.'

try:
    Jeff.check(Joe, 80)    # ValueError: Joe is not a checking account.
except ValueError as e:
    print("non-checking:", e)

Joe.checking_account = True
print(Jeff.check(Joe, 80))    # 'Jeff has 98 and Joe has 40.'

try:
    Joe.check(Jeff, 100)    # ValueError: Jeff has only 98.
except ValueError as e:
    print("bad check:", e)

print(Jeff.add_cash(20.00))    # 'Jeff has 118.'
