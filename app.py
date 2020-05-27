import sys
from password_security import check_password
from password_writer import get_password
from helpers import print_template
from password_generator import add_password
 
if __name__ == "__main__":
    account = sys.argv[1]
    action = sys.argv[2]
    if action == '-a':
        add_password(account)
    elif action == '-g':
        get_password(account)
    elif action == '-s':
        password = get_password(account, prnt=False)
        if password:
            check_password(password)
    else:
        print_template('Invalid command. Try again.')

