from banking.accounts.bank_account import BankAccount
from banking.accounts.savings_account import SavingsAccount
from banking.accounts.current_account import CurrentAccount
from banking.accounts.overdraft_account import OverdraftAccount

import banking.banking_exceptions as ex

class Bank:
    def __init__(self, name,interest_rate):
        self. _name=name
        self.interest_rate=interest_rate
        self._last_id=0
        self._accounts=[]

    def open_account(self, name, password, balance):
        self._last_id+=1
        account = BankAccount(self._last_id, name, password, balance)
        self._accounts.append(account)
        return account._account_number

    def close_account(self, account_number, password):
        account=self._get_account(account_number)
        
        account.authenticate(password)
        
        if account._balance<0:
            raise ex.InsufficentBalanceException(account_number, - account._balance)
        
        self._accounts.remove(account)
        return account._balance
    
    def _get_account(self, account_number):
        for account in self._accounts:
            if account._account_number==account_number:
                return account
        raise ex.InvalidAccountNumberException(account_number,f'Invalid Account {account_number}')

    def deposit(self, account_number, amount):
        account=self._get_account(account_number)
        account.deposit(amount)
        


    def withdraw(self, account_number, amount, password):
        account=self._get_account(account_number)
        account.withdraw(amount, password)
        

    def transfer(self, source_account, amount, password, target_account):
        source=self._get_account(source_account)
        target=self._get_account(target_account)
        
        source.withdraw(amount,password)
        target.deposit(amount)

        

    def get_balance(self, account_number, password):
        account=self._get_account(account_number)
        if account is not None and account.authenticate(password):
            return account._balance
        else:
            return None


    def credit_interest(self):
        for account in self._accounts:
            account.credit_interest(self.interest_rate)


    def get_account_list(self):
        str=''
        for account in self._accounts:
            str+=f'{account}\n'

        return str

