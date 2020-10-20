import json, config, os
from pathlib import Path
from helpers import print_template

path = Path(config.PATH)

def get_data():
    """
    Get account and password data from file.

        Parameters:
            None.

        Returns:
            [] (JSON): Account JSON object.
    """
    if path.exists():
        data = path.read_text()
        return json.loads(data)
    return None

def get_password(account, prnt=True):
    """
    Get password data for a specific account and print it if required.

        Parameters:
            account (string): Account name.
            print (boolean): Set to True by Default. Set to False if no password needs to be printed.

        Returns:
            data[account] (dictonary): Password dictionary object.
    """
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