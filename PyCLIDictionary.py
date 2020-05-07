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
    print("Urban")
    return (responseDict['list'][0]['definition'].replace('[', '').replace(']', ''))

def findWordInData(word):
    print("Non-Urban")
    return data[word]

def findWord():
    fns = [findWordInData, findWordInUrban]
    word = txt.get()

    # window2 = Tk()
    # window2.title(word)
    # window2.geometry('500x250')

    # lbl2 = Label(window2, text="Definition appears here!", wraplength = 500)
    # lbl2.grid(column=0, row=0, columnspan = 100)

    if word in data:
        lbl.configure(text = random.choice(fns)(word))
    elif len(get_close_matches(word, data.keys(), cutoff= 0.75)) > 0:
        c = "Y" # input("Did you mean %s instead? Enter 'Y' or 'N': " % get_close_matches(word, data.keys(), cutoff= 0.75)[0]).upper()
        if c == "Y":
            lbl.configure(text = random.choice(fns)(get_close_matches(word, data.keys(), cutoff= 0.75)[0]))
        else:
            lbl.configure(text = "Oops! Try Again.")
    else:  
        lbl.configure(text = "Word not found, please try another word. ")

window = Tk()
window.title("Reliable Dictionary")
window.configure(bg = "white")
window.geometry('500x250')

logoPhoto = Image.open("logo.png")
logoPhoto = logoPhoto.resize((240, 100), Image.ANTIALIAS)
photoImg =  ImageTk.PhotoImage(logoPhoto)


logo = Label(window, image = photoImg, background = "white")    
logo.grid(column = 0, row = 1, columnspan = 100, rowspan = 5, pady = 1, padx = 125, sticky = "wens")

lbl = Label(window, text="the label appears here!", wraplength=480, background = "white")
lbl.grid(column=0, row=7, columnspan = 100)

window.grid_columnconfigure((0, 1, 2), weight=1)

txt = Entry(window,width=10)
txt.grid(column=0, columnspan = 2, row=6, sticky = "ew")

btn = Button(window, text="Find Definitions", command= findWord)
btn.grid(column=2, row=6, sticky = "ew")

window.mainloop()