import json, config, os, pyperclip
from pathlib import Path
from password_retrieval import get_data
from password_generator import generate_password
from helpers import print_template

path = Path(config.PATH)

#write the account and password dictionary object to file
def add_password(account):
    fetched_data = get_data()
    new_password = generate_password()
    #if there is data, change existing dictionary item or create a new one. 
    # If there is no data, create a new file and write new item to it.
    if fetched_data is not None:
        if account in fetched_data:
            print_template(f"The password for your '{account}' account has been changed. \nPassword copied to clipboard...")
        else:
            print_template(f"A password for your '{account}' account has been created. \nPassword copied to clipboard...")
        write_to_file(account, new_password, fetched_data)
    else:
        write_to_file(account, new_password)
        print_template(f"Password file created. \nA password for your '{account}' account has been created. \nPassword copied to clipboard...")
    pyperclip.copy(new_password)

#write account data to file
def write_to_file(account, password, data={}):
    data[account] = password
    data_to_write = json.dumps(data)
    path.write_text(data_to_write)
