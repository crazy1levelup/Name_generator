from string import ascii_lowercase, ascii_letters
from random import choice

#print help(string) to see what the module does
print ascii_letters #this contain all upper and lower case letters
print ascii_lowercase #this contain all lower case letters

letter_input1 = raw_input("Chose a letter...'v' for vowels, 'c' for consonants, 'l' for any other letter: ")
letter_input2 = raw_input("Chose a letter...'v' for vowels, 'c' for consonants, 'l' for any other letter: ")
letter_input3 = raw_input("Chose a letter...'v' for vowels, 'c' for consonants, 'l' for any other letter: ")
letter_input4 = raw_input("Chose a letter...'v' for vowels, 'c' for consonants, 'l' for any other letter: ")
letter_input5 = raw_input("Chose a letter...'v' for vowels, 'c' for consonants, 'l' for any other letter: ")

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letter = ascii_lowercase

def generator():
    if letter_input1 == "v":
        letter1 = choice(vowels)
    elif letter_input1 == "c":
        letter1 = choice(consonants)
    elif letter_input1 == "l":
        letter1 = choice(letter)
    else:
        letter1 = letter_input1 #this allows the user to select any other letter

    if letter_input2 == "v":
        letter2 = choice(vowels)
    elif letter_input2 == "c":
        letter2 = choice(consonants)
    elif letter_input2 == "l":
        letter2 = choice(letter)
    else:
        letter2 = letter_input2 #this allows the user to select any other letter

    if letter_input3 == "v":
        letter3 = choice(vowels)
    elif letter_input3 == "c":
        letter3 = choice(consonants)
    elif letter_input3 == "l":
        letter3 = choice(letter)
    else:
        letter3 = letter_input3 #this allows the user to select any other letter

    if letter_input4 == "v":
        letter4 = choice(vowels)
    elif letter_input4 == "c":
        letter4 = choice(consonants)
    elif letter_input4 == "l":
        letter4 = choice(letter)
    else:
        letter4 = letter_input4 #this allows the user to select any other letter

    if letter_input5 == "v":
        letter5 = choice(vowels)
    elif letter_input5 == "c":
        letter5 = choice(consonants)
    elif letter_input5 == "l":
        letter5 = choice(letter)
    else:
        letter5 = letter_input5 #this allows the user to select any other letter

    name = letter1 + letter2 + letter3 + letter4 + letter5
    return name

for numbers in range(10):
    print generator()


