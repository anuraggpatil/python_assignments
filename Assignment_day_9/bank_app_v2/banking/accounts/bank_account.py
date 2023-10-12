import banking.banking_exceptions as ex

class BankAccount: #BankAccount is NOT a type of Bank
    def __init__(self, accountNumber, name, password, balance):
        self._account_number=accountNumber
        self._name=name
        self._password=password
        self._balance=balance

    def authenticate(self, password):
        if password!=self._password:
            raise ex.InvalidCredentialsException(self._account_number, 'Invalid Credentials')
        

    def change_password(self, oldPassword, newPassword):
        self.authenticate(oldPassword)
        #if we reach here, that means authenticatio is success
        self._password=newPassword
       
    def _validate_amount(self, amount):
        if amount<0:
            raise ex.InvalidDenominationException(self._account_number,'Amount Must be Positive')

    def deposit(self, amount):
        self._validate_amount(amount)
        self._balance+=amount

    def withdraw(self, amount, password):
        self._validate_amount(amount)
        self.authenticate(password)

        if self._account_type=="SAVINGS" and amount> self._balance-5000:
            raise ex.InsufficentBalanceException(self.address, amount-self._balance-5000)
        elif self._account_type=="OD" and amount> self._balance+self._od_limit:
            raise ex.InsufficentBalanceException(self.address, amount-self._balance-5000)
        if amount>self._balance:
            raise ex.InsufficentBalanceException(self._account_number, amount-self._balance)
        
        self._balance-=amount
            
    def credit_interest(self,interest_rate):
        self._balance+=(self._balance*interest_rate)/1200

    #def info(self):
    def __str__(self):
        return f'BankAccont[AccountNumber={self._account_number},Name={self._name},Balance={self._balance}]'