#94 02:32
import sys
import requests
import random
import json
from difflib import get_close_matches #for comparing strings!

data = json.load(open("data.json"))

# Urban Dictionary API
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "f7c2d6c1admshf9511bb1a414560p12dbdbjsn06ce2a38118a"
    }

def findWordInUrban(word):
    querystring = {"term": word}
    response = requests.request("GET", url, headers=headers, params=querystring)
    responseDict = json.loads(response.text)
    return (responseDict['list'][0]['definition'])

def findWordInData(word):
    return data[word]

def findWord(word):
    fns = [findWordInData, findWordInUrban]
    if word in data:
        return random.choice(fns)(word)
    elif len(get_close_matches(word, data.keys(), cutoff= 0.75)) > 0:
        c = input("Did you mean %s instead? Enter 'Y' or 'N': " % get_close_matches(word, data.keys(), cutoff= 0.75)[0]).upper()
        if c == "Y":
            return random.choice(fns)(get_close_matches(word, data.keys(), cutoff= 0.75)[0])
        else:
            return "Oops! Try Again."
    else:  
        return "Word not found, please try another word. "

while(True):   
    userInput = input("Enter a word: ").lower()
    print(findWord(userInput))
    if (input("Enter 'E' to exit: ").upper() == 'E'):
        sys.exit()