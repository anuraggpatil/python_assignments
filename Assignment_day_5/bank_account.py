# Create a model for represening a bank account 
# It should have 
    # account number 
    # name 
    # password 
    # balance 
    # interest rate 
# It should support 
    # deposit 
        # should fail for negative maount 
    # withdraw 
        # should fail if 
            # amount <0 
            # amount>balance 
            # wrong password 
    # credit interest 
        # credits one month interest using forumula 
            # balance+=(balance*rate/1200) 
    # info 

import random as r

class BankAccount:
    pass

def show_info(account):
    if not is_valid(account):
        return print('<invalid account>')
    print('Following are the details of your bank account:')
    print(f'Name: {account.name}')
    print(f'Account No.: {account.account_num}')
    print(f'Balance: {account.balance}')
    print()

def is_valid(account):
    if isinstance(account, BankAccount):
        if account.balance>=0:
            return True
    return False
    

def create_bank_account(name, password, balance):
    account = BankAccount()
    account.name = name
    account.password = password
    account.balance = balance
    account.account_num = r.randint(100, 999)

    if not is_valid(account):
        return print('<invalid account>')

    print(f'Thank You for creating an account with us {account.name} :)\n')
    show_info(account)

    return account

def get_details(account, password):
    if not is_valid(account):
        return print('<invalid account>')
    if password == account.password:
        show_info(account)
    else:
        print('The password is incorrect!')

def deposit_money(account, amount):
    if not is_valid(account):
        return print('<invalid account>')
    if amount>0:
        account.balance += amount
        print(f'Money successfully deposited, current balance is {account.balance}\n')
    else:
        print('Please enter a valid input')

def withdraw_money(account, amount, password):
    if not is_valid(account):
        return print('<invalid account>')
    if password == account.password:
        if amount>account.balance:
            print('Not enough balance, please enter valid input')
        else:
            if amount>0:
                account.balance -= amount
                print(f'Successfully Withdrawn {amount}, remaining balance is {account.balance}\n')
            else:
                print('Please enter a valid input')
    else:
        print('Incorrect Password!')



a1 = create_bank_account('Anurag', 'pass123', 1000)

a2 = create_bank_account('sid', 'abc', 0)

deposit_money(a1, 1500)
withdraw_money(a1, 500, 'pass123')

get_details(a2, 'abc')