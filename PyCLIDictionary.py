#94 02:32
import json
from difflib import get_close_matches #for comparing strings!

data = json.load(open("data.json"))

def findWordInDict(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff= 0.75)) > 0:
        choice = input("Did you mean %s instead? Enter 'Y' or 'N': " % get_close_matches(word, data.keys(), cutoff= 0.75)[0]).upper()
        if choice == "Y":
            findWordIndict(get_close_matches(word, data.keys(), cutoff= 0.75)[0])


    else:
        return "Word not found :( "

userInput = input("Enter a word: ").lower()

print(findWordInDict(userInput))