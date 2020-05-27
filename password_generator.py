import string, json, requests
from random import randint, choice
from helpers import print_template

def generate_words():
    url = requests.get("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
    words = json.loads(url.text)
    return [choice(words) for n in range(4)]

#generate a random password
def generate_password():
    word_list = generate_words()

    #generate random index, special characters, and numbers
    random_index = [randint(0,3) for r in range(0,5)]
    random_special_character = [choice("!@#$%^&*()_") for c in range(2)]
    random_number = [choice(string.digits) for n in range(2)]

    #UPPERcase random word in list
    word_list[random_index[0]] =  word_list[random_index[0]].upper()

    #add special characters to random index
    word_list.insert(random_index[1], random_special_character[0])
    word_list.insert(random_index[2], random_special_character[1])

    #add number to random index
    word_list.insert(random_index[3], random_number[0])
    word_list.insert(random_index[4], random_number[1])

    #join the list together and strip whitespace to create a random password
    combined_random_password = ''.join(word_list)
    random_password = combined_random_password.replace(" ", "")

    return random_password