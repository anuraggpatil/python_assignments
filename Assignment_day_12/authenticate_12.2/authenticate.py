from suppress_exception import supress_exception

users = dict()

@supress_exception
def authenticate(user, password):
    print(f'authenticating user {user}')
    return users[user] == password

def main():
    users.__setitem__('Anurag', 'pass')
    users.__setitem__('Nik', 'p@ss')
    users.__setitem__('Vivek', 'abc')
    

    print(authenticate('Anurag', 'p@ss'))

if __name__ == '__main__':
    main()