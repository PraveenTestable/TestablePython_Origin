class Account:
    def __init__(self, id, owner, balance):
        self.id = id
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, id, owner, balance=0):
        account = Account(id, owner, balance)
        self.accounts[id] = account
        return account

    def deposit(self, id, amount):
        self.accounts[id].deposit(amount)

    def withdraw(self, id, amount):
        self.accounts[id].withdraw(amount)

    def get_balance(self, id):
        return self.accounts[id].get_balance()

    def transfer(self, from_id, to_id, amount):
        self.withdraw(from_id, amount)
        self.deposit(to_id, amount)
