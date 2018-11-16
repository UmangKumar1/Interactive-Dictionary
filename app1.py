#import all the packages you need
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
#prompt the user to enter the word they want to look up
inputName = input("Which word would you like the definition for?  ")
inputName = inputName.lower()
#open your dictionary file and set the dictionary to a variable so you can manipulate it
data = json.load(open("data.json"))

#This function takes the inputName and tells you the definition, if there is no such word in the dictionary, it looks for the closest related word
def translate(word):
#simply checks if the word is in dictionary and if it is gives back the definition
    if word in data:
        return data[word]
#gets the closest word in the dictionary witht he get_close_match function and asks if that is the word you were looking for
    elif get_close_matches(word,data.keys()) > 0:
        closeWord = get_close_matches(word,data.keys(), n = 10)[0]
        changeName = input("That is a not a word, are you sure you didnt mean:: " + closeWord + " ?? (Enter Y for yes/ N for no) :")
        if changeName == "Y":
            return data[closeWord]
        elif changeName == "N":
            return "Not a word!"
#Sends back generic message if none of the prior 2 were wrong
    else:
        return "This is not a word"
#calls the translate function with the word you input and prints it
print(translate(inputName))
