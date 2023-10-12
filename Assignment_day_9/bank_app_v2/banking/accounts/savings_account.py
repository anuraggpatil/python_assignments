from banking.accounts.bank_account import BankAccount
import banking.banking_exceptions as ex

class SavingsAccount(BankAccount):
    def withdraw(self, amount, password):
        self._validate_amount(amount)
        self.authenticate(password)
        if amount > self._balance-5000:
            raise ex.InsufficentBalanceException(self._account_number, amount - self._balance - 5000)
        self._balance-=amount