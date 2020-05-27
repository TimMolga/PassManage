import json, config, os
from pathlib import Path
from helpers import print_template

path = Path(config.PATH)

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
    else:
        print_template(f"No password file exists.")