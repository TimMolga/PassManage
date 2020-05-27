import json, config, os
from pathlib import Path
from helpers import print_template

path = Path(config.PATH)

#write the account and password dictionary object to file
def write_password(account, password):
    fetched_data = get_data()
    #if there is data, change existing dictionary item or create a new one. 
    # If there is no data, create a new file and write new item to it.
    if fetched_data is not None:
        if account in fetched_data:
            print_template(f"The password for your '{account}' account has been changed. \nPassword copied to clipboard...")
        else:
            print_template(f"A password for your '{account}' account has been created. \nPassword copied to clipboard...")
        write_to_file(account, password, fetched_data)
    else:
        write_to_file(account, password)
        print_template(f"Password file created. \nA password for your '{account}' account has been created. \nPassword copied to clipboard...")

#write account data to file
def write_to_file(account, password, data={}):
    data[account] = password
    data_to_write = json.dumps(data)
    path.write_text(data_to_write)

#check if file exists and get data
def get_data():
    if path.exists():
        data = path.read_text()
        return json.loads(data)

#get the password for the specific account
def get_password(account, prnt=True):
    data = get_data()
    if data is not None:
        if account in data:
            if prnt:
                print_template(f"Your password for '{account}' is {data[account]}.")
            return data[account]
        else:
            print_template(f"A password for '{account}' does not exist. Try again.")

