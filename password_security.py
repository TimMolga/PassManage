import requests, hashlib, sys, re
from bs4 import BeautifulSoup
from password_retrieval import get_password
from helpers import print_template

#create the intial 5 hash characters for the pwned api
def hash_password(password_to_hash):
    hash_password = hashlib.sha1(str(password_to_hash).encode('utf-8')).hexdigest()
    return hash_password[0:5]

#check the hash value on pwned api, provide a final count as well as the worst password hash value
def check_pwned_api(password_to_check):
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

#reverse the sha1 to find the most 
def reverse_sha1(partial_hash, remainder_hash):
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

