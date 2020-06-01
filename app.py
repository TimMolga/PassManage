import sys
from password_security import check_password_security
from password_retrieval import get_password
from password_writer import add_password
from helpers import print_template

if __name__ == "__main__":
    account = sys.argv[1]
    action = sys.argv[2]
    if action == '-a':
        add_password(account)
    elif action == '-g':
        get_password(account)
    elif action == '-s':
        check_password_security(account)
    else:
        print_template('Invalid command. Try again.')