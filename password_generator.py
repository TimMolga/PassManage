import string, pyperclip
from random import randint, choice
from random_word import RandomWords
from password_writer import write_password

#generate a random password
def generate_password():
    #generate random words
    r = RandomWords()
    word_list = r.get_random_words(hasDictionaryDef="true", limit=4)

    #generate random index, numbers and special characters
    random_integer = [randint(0,3) for r in range(0,5)]
    random_special_character = [choice("!@#$%^&*()_") for c in range(2)]
    random_number = [choice(string.digits) for n in range(2)]

    #UPPERcase random word in list
    word_list[random_integer[0]] =  word_list[random_integer[0]].upper()

    #add special characters to random index
    word_list.insert(random_integer[1], random_special_character[0])
    word_list.insert(random_integer[2], random_special_character[1])

    #add number to random index
    word_list.insert(random_integer[3], random_number[0])
    word_list.insert(random_integer[4], random_number[1])

    #join the list together and strip whitespace to create a random password
    combined_random_password = ''.join(word_list)
    random_password = combined_random_password.replace(" ", "")

    return random_password

#add the password to file and add to clipboard
def add_password(account):
    new_password = generate_password()
    write_password(account, new_password)
    pyperclip.copy(new_password)