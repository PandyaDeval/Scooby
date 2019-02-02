from __future__ import print_function
import speech_recognition as sr
import speech
from os import path
from pywinauto import Desktop, Application
from pywinauto.keyboard import SendKeys, KeySequenceError
from pywinauto.timings import wait_until
import re, time
import spacy
import speech_recognition as sr
import pyaudio
import PIL
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract

nlp=spacy.load('en') 

def noun(x):
    nounlist=[]
    for token in x:
        if token.pos_=='NOUN':
            nounlist.append(token.text)
    return nounlist
def adj(x):
   adjlist=[]
   for token in x:
       if token.pos_=='ADJ':
           adjlist.append(token.text)
   return adjlist
def verb(x):
    verblist=[]
    for token in x:
        if token.pos_=='VERB':
            verblist.append(token.text)
    return verblist
#query = str('start mozilla')       #converting speech to text using speech_to_text API 


def start_app(app_name):
    try:
        app=Application().start(app_name)
        apps.append(app)
    
    except:
        with open("paths.txt") as f:
            for line in f:
                try:
                    line=re.split("-",line,1)
                    app_path = line[1][:-1] + app_name
                    #print(app_path)
                    app=Application().start(app_path + " --renderer-force-accessibility")
                    break
                except:
                    continue
                    


query = str(speech.press_record())       #converting speech to text using speech_to_text API 

print(query) 

doc=nlp(query)

if not noun(doc):
    pass
else:
    name=noun(doc)[0]
if not adj(doc):
    pass
else:
    task=adj(doc)[0]
  
if not verb(doc):
    pass
else:
    do=verb(doc)[0]
from spacy.lang.en.stop_words import STOP_WORDS
words=[word.text.lower() for word in doc if word.is_stop==False]

print(words)

verb, obj = words
token=nlp("start")
similarity = token.similarity(nlp(verb))
print(similarity)
apps=[]
if float(similarity)>0.5:
    start_app(obj)
time.sleep(2)
img = PIL.ImageGrab.grab()
imgplot = plt.imshow(img)