class BankAccount:
    def __init__(self, initialamount, accountname):
        self.balance = initialamount
        self.name = accountname
        print(f'\nAccount {self.name} created.\nBalance = ${self.balance:.2f}')


