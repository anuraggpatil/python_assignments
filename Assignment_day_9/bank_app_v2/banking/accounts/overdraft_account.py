from banking.accounts.bank_account import BankAccount

class OverdraftAccount:
    def __init__(self, accountNumber, name, password, balance):
        super.__init__(accountNumber, name, password, balance)
        self._max_balance = balance
    def withdraw(self, amount, password):
        
        od_limit = self.max_balance * 0.1
        if amount<0:
            return False
        elif amount>self._balance+od_limit:
            return False
        elif not self.authenticate(password):
            return False
        
        if amount <= self._balance:
            self._balance -= amount
        elif amount <= self._balance + od_limit:
            od_fee = amount * 0.01
            self._balance -= amount - od_fee

    def deposit(self, amount):
        if amount>0:
            self._balance+=amount
            self._max_balance = max(self._max_balance, self._balance)
            return True
        else:
            return False