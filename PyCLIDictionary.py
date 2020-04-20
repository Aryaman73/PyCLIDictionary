#94 02:32
import sys
import requests
import random
import json
from difflib import get_close_matches #for comparing strings!
from tkinter import *

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

# def findWord2():
#     lbl.configure(text= txt.get())

def findWord():
    fns = [findWordInData, findWordInUrban]
    word = txt.get()
    if word in data:
        lbl.configure(text = random.choice(fns)(word))
    elif len(get_close_matches(word, data.keys(), cutoff= 0.75)) > 0:
        c = input("Did you mean %s instead? Enter 'Y' or 'N': " % get_close_matches(word, data.keys(), cutoff= 0.75)[0]).upper()
        if c == "Y":
            lbl.configure(text = random.choice(fns)(get_close_matches(word, data.keys(), cutoff= 0.75)[0]))
        else:
            lbl.configure(text = "Oops! Try Again.")
    else:  
        lbl.configure(text = "Word not found, please try another word. ")
    

# while(True):   
#     userInput = input("Enter a word: ").lower()
#     print(findWord(userInput))
#     if (input("Enter 'E' to exit: ").upper() == 'E'):
#         sys.exit()


window = Tk()
window.title("Reliable Dictionary")
window.geometry('500x250')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=1)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="Find Definitions", command= findWord)
btn.grid(column=2, row=0)

window.mainloop()