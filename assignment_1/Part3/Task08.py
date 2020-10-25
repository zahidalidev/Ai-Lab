# a)
# In this exercise, the task is to write a function that picks a random word from a list of
# words below. listOfWords = [APPLE, BILBO, CHORUSED, DISIMAGINE,
# ENSURING, FORMALISING, GLITCHES, HARMINE, INDENTATION, JACKED,
# KALPACS, LAUNDRY, MASKED, NETTED, OXFORD, PARODY, QUOTIENTS,
# RACERS, SADNESS, THYREOID, UNDUE, VENT, WEDGED, XERIC, YOUTHHOOD,
# ZIFFS]
# Hint: use the Python random library for picking a random word.

import random

listOfWords = ["APPLE", "BILBO", "CHORUSED", "DISIMAGINE",
               "ENSURING", "FORMALISING", "GLITCHES", "HARMINE", "INDENTATION", "JACKED",
               "KALPACS", "LAUNDRY", "MASKED", "NETTED", "OXFORD", "PARODY", "QUOTIENTS",
               "RACERS", "SADNESS", "THYREOID", "UNDUE", "VENT", "WEDGED", "XERIC", "YOUTHHOOD",
               "ZIFFS"]


def pick_random_word(list):
    index = random.randint(0, len(list))
    return list[index]


random_word = pick_random_word(listOfWords)
print("\nRandom Word:", random_word)


# b)
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the
# program that the player has to guess, letter by letter. The player guesses one letter at a
# time until the entire word has been guessed. (In the actual game, the player can only
# # guess 6 letters incorrectly before losing).

print("\nWelcome to Hangman Part B")

word = random_word    # random word fom above function
dashes = "_" * len(word)  # dashes of length of word
character_guessed_and_dashes = list(dashes)

characters = list(word)

incorrect_count = 0
guessed_list = []

while True:
    letter = input("\nguess letter: ")

    if characters.__contains__(letter.upper()) == False:
        incorrect_count = incorrect_count + 1

    if(incorrect_count == 6):
        print("You Loose")
        break

    elif letter.upper() in guessed_list:
        letter = ''
        print("This character is already guessed try again")

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
        print("\n******************* YOU WON ******************\n")
        break
