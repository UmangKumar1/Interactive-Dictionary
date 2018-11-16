import json
import difflib

from difflib import SequenceMatcher
from difflib import get_close_matches

inputName = input("Which word would you like the definition for?  ")
inputName = inputName.lower()

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:

        closeWord = get_close_matches(word,data.keys(), n = 10)[0]
        changeName = input("That is a not a word, are you sure you didnt mean:: " + closeWord + " ?? (Enter 1 for yes) :")
        if changeName == "1":
            return data[closeWord]
        else:
            while changeName != "1":
                x = 0
                closeWord = get_close_matches(word,data.keys(), n=10)[x]
                x = x+1
                changeName = input("What about: " + closeWord + " ?? (Enter 1 for yes) :")
            return data[closeWord]





print(translate(inputName))
