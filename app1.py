import json

inputName = input("Which word would you like the definition for?  ")
inputName = inputName.lower()

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    else:
        return "Word is not in the dictionary"


print(translate(inputName))
