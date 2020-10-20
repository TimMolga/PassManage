import requests, hashlib, sys, re
from bs4 import BeautifulSoup
from password_retrieval import get_password
from helpers import print_template

def hash_password(password_to_hash):
    """
    Create the intial 5 hash characters for the PWNED API.

        Parameters:
            password_to_hash (string): Password to transform into a hash.

        Returns:
            hash_password (list): Hashed password from PWNED.
    """
    hash_password = hashlib.sha1(str(password_to_hash).encode('utf-8')).hexdigest()
    return hash_password[0:5]

def check_pwned_api(password_to_check):
    """
    Check the hash value on PWNED API, sum of worst passwords and the worst password hash value.

        Parameters:
            password_to_check (string): Hashed password to check on the PWNED API.

        Returns:
            [] (list): Number of worst passwords based on hash, and worst password hash value.
    """
    #check api and get text response
    pwned_url = f"https://api.pwnedpasswords.com/range/{password_to_check}"
    pwned_response = requests.get(pwned_url)
    passwords = pwned_response.text

    #parse text response to get hash count
    lines = passwords.splitlines(False)
    string_count = [item.split(':', 1)[1] for item in lines]
    number_count = [int(item) for item in string_count]
    final_sum = sum(number_count)

    #get hash value of worst password
    worst_password_count = max(number_count)
    worst_password_index = number_count.index(worst_password_count)

    return (final_sum, (lines[worst_password_index]).split(':')[0])

def reverse_sha1(partial_hash, remainder_hash):
    """
    Reverse the sha1 to find the worst password with this hash.

        Parameters:
            partial_hash (string): Partial hash to combine with remainder hash to reverse hash.
            remainder_hash (string): Remainder hash to combine with partial hash to reverse hash.

        Returns:
            password (string): Worst password based on hash.
    """
    #format parameters and get site details
    params = {
        "hash" : partial_hash + remainder_hash
    }
    sha1_url = "https://sha1.gromweb.com/"
    sha1_response = requests.get(sha1_url, params=params)
    sha1 = sha1_response.text

    #parse html page with beautiful soup and return value
    soup = BeautifulSoup(sha1, 'html.parser')
    worst_password_class = soup.find_all("em", class_="long-content string")
    worst_password_string = str(worst_password_class)
    try:
        return "\"" + re.split('>|<', worst_password_string)[2] + "\""
    except IndexError:
        return False

# run functions and print output
def check_password_security(account):
    """
    Run functions and print output.

        Parameters:
        account (string): Account password to check.

        Returns:
            None.
    """
    password = get_password(account, prnt=False)
    if password:
        partial_password = hash_password(password)
        pwned_api_value = check_pwned_api(partial_password)
        worst_password_param = pwned_api_value[1]
        final_sum = pwned_api_value[0]
        worst_password = reverse_sha1(partial_password, worst_password_param)

        if worst_password:      
            content = f'''The password beginning with \"{partial_password}\" appeared {final_sum:,} times. \nThe worst password beginning with this hash was {worst_password}.'''
            print_template(content)
        else:
            content = f'''The password beginning with \"{partial_password}\" appeared {final_sum:,} times. \nThe worst password beginning with this hash was unable to be reversed.'''
            print_template(content)

