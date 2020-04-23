#94 02:32
import sys
import requests
import random
import json
from difflib import get_close_matches #for comparing strings!
from tkinter import *
from tkinter.ttk import *
from PIL import Image
from PIL import ImageTk


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

    window2 = Tk()
    window2.title(word)
    window2.geometry('500x250')

    lbl2 = Label(window2, text="Definition appears here!", wraplength = 500)
    lbl2.grid(column=0, row=0, columnspan = 100)

    if word in data:
        lbl2.configure(text = random.choice(fns)(word))
    elif len(get_close_matches(word, data.keys(), cutoff= 0.75)) > 0:
        c = input("Did you mean %s instead? Enter 'Y' or 'N': " % get_close_matches(word, data.keys(), cutoff= 0.75)[0]).upper()
        if c == "Y":
            lbl2.configure(text = random.choice(fns)(get_close_matches(word, data.keys(), cutoff= 0.75)[0]))
        else:
            lbl2.configure(text = "Oops! Try Again.")
    else:  
        lbl2.configure(text = "Word not found, please try another word. ")
    

# while(True):   
#     userInput = input("Enter a word: ").lower()
#     print(findWord(userInput))
#     if (input("Enter 'E' to exit: ").upper() == 'E'):
#         sys.exit()


window = Tk()
window.title("Reliable Dictionary")
window.configure(bg = "white")
window.geometry('500x250')

logoPhoto = Image.open("logo.png")
logoPhoto = logoPhoto.resize((240, 100), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(logoPhoto)


logo = Label(window, image = photoImg)
logo.grid(column = 0, row = 1, columnspan = 100, rowspan = 5, pady = 1, padx = 125, sticky = "wens")

lbl = Label(window, text="Definition appears here!")
lbl.grid(column=0, row=7, columnspan = 100)

window.grid_columnconfigure((0, 1, 2), weight=1)

txt = Entry(window,width=10)
txt.grid(column=0, columnspan = 2, row=6, sticky = "ew")

btn = Button(window, text="Find Definitions", command= findWord)
btn.grid(column=2, row=6, sticky = "ew")

window.mainloop()