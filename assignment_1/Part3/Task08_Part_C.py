# c) In this exercise, we will finish building Hangman. In the game of Hangman, the player only
# has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic
# for guessing the letter and displaying that information to the user. In this exercise, we have to
# put it all together and add logic for handling guesses.

import random

print("\nWelcome to Hangman Part C")

listOfWords = ["APPLE", "BILBO", "CHORUSED", "DISIMAGINE",
               "ENSURING", "FORMALISING", "GLITCHES", "HARMINE", "INDENTATION", "JACKED",
               "KALPACS", "LAUNDRY", "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS",
               "RACERS", "SADNESS", "THYREOID", "UNDUE", "VENT", "WEDGED", "XERIC", "YOUTHHOOD",
               "ZIFFS"]


def pick_random_word(list):
    index = random.randint(0, len(list))
    return list[index]


random_word = pick_random_word(listOfWords)


word = "HHHHH"    # random word fom above function
dashes = "_" * len(word)  # dashes of length of word
character_guessed_and_dashes = list(dashes)

characters = list(word)

incorrect_count = 0
guessed_list = []

while True:
    letter = input("\nguess letter: ")

    if letter.upper() in guessed_list:
        print("This character is already guessed try again")
    elif characters.__contains__(letter.upper()) == False:
        incorrect_count = incorrect_count + 1
        print("You have", 6 - incorrect_count, "guesses left")

    if(incorrect_count == 6):
        print("You Loose")
        break

    elif letter.upper() in guessed_list:
        letter = ''

    elif letter.upper() in characters:
        index = characters.index(letter.upper())
        character_guessed_and_dashes[index] = letter.upper()
        characters[index] = '_'
        print(character_guessed_and_dashes)

    else:
        print(''.join(character_guessed_and_dashes))
        if letter is not '':
            guessed_list.append(letter.upper())

    if '_' not in character_guessed_and_dashes:
        print("\n\n******************* YOU WON ******************\n")
        break
