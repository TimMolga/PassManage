def hasNumber(string):
    return any(char.isdigit() for char in string)

def hasSpecialCharacter(string):
    return any(not char.isalnum() for char in string)

def hasUppercase(string):
    return any(char.isupper() for char in string)