# Write a password generator in Python. Be creative with how you generate passwords - strong
# passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The
# passwords should be random, generating a new password every time the user asks for a new
# password. Include your run-time code in a main method.
# Extra:
#  Ask the user how strong they want their password to be. For weak passwords, pick a word or
# two from a list.

import string
import random


def generatePassword(level):
    length = 1
    if level == "low":
        length = 2
    elif level == 'medium':
        length = 4
    elif level == 'hight':
        length = 6

    symbols = [random.choice(string.punctuation)
               for i in range(length)]
    lowercase_letters = [random.choice(string.ascii_lowercase)
                         for i in range(length)]
    uppercase_letters = [random.choice(string.ascii_uppercase)
                         for i in range(length)]
    numbers = [random.choice(string.digits)
               for i in range(length)]

    generatedPassword = symbols + lowercase_letters + uppercase_letters + numbers
    random.shuffle(generatedPassword)
    return ''.join(generatedPassword)


def main():
    level = input('Please enter the Level low, medium or hight: ')
    password = generatePassword(level)
    print(password)


if __name__ == "__main__":
    main()
