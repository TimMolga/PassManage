import string, sys
from password_security import check_password
from random import randint, choice
from password_writer import get_password
from helpers import print_template
from password_generator import add_password
 
if __name__ == "__main__":
    account = sys.argv[1]
    action = sys.argv[2]
    if action == '-a':
        add_password(account)
        print_template('Password copied to clipboard...')
    elif action == '-g':
        password = get_password(account)
        if password:
            print_template(password)
        else:
            print_template('That account does not exist. Try again.')
    elif action == '-s':
        password = get_password(account)
        if password:
            check_password(password)
        else:
            print_template('That account does not exist. Try again.')
    else:
        print_template('Invalid command. Try again.')

