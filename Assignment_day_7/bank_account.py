
class Bank:
    def __init__(self, bank_name):
        self._bank_name = bank_name

    def open_account(self, name, password, amount, account_type):
        try:
            account = BankAccount(name, password, amount, account_type)
            if account._account_type == 'Savings':
                return account if self.correct_savings_account_details(account) else print('<can\'t open account>')
            elif account._account_type == 'Current':
                return account if self.correct_current_account_details(account) else print('<can\'t open account>')
            elif account._account_type == 'Overdraft':
                return account if self.correct_overdraft_account_details(account) else print('<can\'t open account>') 
            else:
                print('enter valid account type')
        except:
            print('<invalid_details>')           
            
    
    def correct_savings_account_details(self, account):
        return  True if account._balance >= 5000 else False
        
    def correct_current_account_details(self, account):
        return True if account._balance >= 0 else False
    
    def correct_overdraft_account_details(self, account):
        return True if account._balance >= 0 else False

    def deposit_to_account(self, account, amount):
        account.deposit_money(amount)
    

class BankAccount:
    def __init__(self, name, password, amount, account_type):
        self._name = name
        self.__password = password
        self._balance = amount
        self._account_type = account_type
        if(account_type == 'Overdraft'):
            self.max_balance = self._balance

    def is_valid_password(self, password):
        return True if self.__password == password else False

    def deposit_money(self, amount):
        self._balance += amount
        
        if self._account_type == 'Overdraft' and self._balance > self.max_balance:
            self.max_balance = self._balance

    def withdraw_money_from_savings(self, amount):
        if amount<= self._balance-5000:
            self._balance -= amount

        else: print('<not enough balance>')

    def withdraw_money_from_current(self, amount):
        if amount<= self._balance:
            self._balance -= amount
        else: print('<not enough balance>')

    def withdraw_money_from_overdraft(self, amount):
        od_limit = self.max_balance * 0.1
        
        if amount <= self._balance:
            self._balance -= amount
        elif amount <= self._balance + od_limit:
            od_fee = amount * 0.01
            self._balance -= amount - od_fee
        else: print('<not enough balance>')
        
class ATM:
    def get_account_info(self, account):
        try:
            print(f"Holder's Name: {account._name}")
            print(f'Amount: {account._balance}')
            print(f'Account type: {account._account_type}')
        except:
            print('<invalid_account>')

    def withdraw_money(self, account, password, amount):
        try:
            if not account.is_valid_password(password):
                print('<invalid_password>')
                return
            if account._account_type == 'Savings':
                account.withdraw_money_from_savings(amount)
            elif account._account_type == 'Current':
                account.withdraw_money_from_current(amount)
            else:
                account.withdraw_money_from_overdraft(amount)
        except:
            print('<invalid_account_details>')
    
    def transfer_money(self, account1, password, amount, account2):
        try:
            self.withdraw_money(account1, password, amount)
            account2.deposit_money(amount)
        except:
            print('<invalid_account_details>')
            


icici = Bank('ICICI')

a1 = icici.open_account('Vivek', 'p@ss', 50000, 'Savings')
a2 = icici.open_account('Sanjay', 'p@ss', 50000, 'Overdraft')
atm = ATM()
atm.withdraw_money(a1, 'p@ss', 20000)
atm.transfer_money(a2, 'p@ss', 10000, a1)

atm.get_account_info(a1)
atm.get_account_info(a2)