from __future__ import print_function
import speech_recognition as sr
import speech
from os import path
from pywinauto import Desktop, Application
from pywinauto.keyboard import SendKeys, KeySequenceError
#from pywinauto.timings import wait_until
from pywinauto import mouse
import re, time, math
import spacy
import speech_recognition as sr
import pyaudio
from PIL import Image, ImageDraw, ImageFont
import PIL
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract
from spacy.lang.en.stop_words import STOP_WORDS
import winsound
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

frequency = 1500
duration = 1000

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('Roboto-Bold.ttf', size=10)
nlp=spacy.load('en') 
nlp.vocab["go"].is_stop = False
nlp.vocab["back"].is_stop = False
nlp.vocab["all"].is_stop = False
#print(nlp.Defaults.stop_words)
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
                    
def user_single_click(text):
    time.sleep(0.5)
    img = PIL.ImageGrab.grab()
    #imgplot = plt.imshow(img)
    data=pytesseract.image_to_data(img)

    data=data.split()
    #print(data)
    
    for i in range(len(data)):
        if ' '.join(text) in data[i].lower():
            print("Match Found")
            #coord_x = int(data[i-5]) + int(data[i-3]/2)
            #coord_y = int(data[i-4]) + int(data[i-2]/2)
            coord_x = int(data[i-5]) + int(int(data[i-3])/2)
            coord_y = int(data[i-4]) + int(int(data[i-2])/2)
            mouse.click(button="left",coords=(coord_x,coord_y))
            print("Mouse Clicked at: (" ,coord_x,",", coord_y,")")
            break
        
def user_double_click(text):
    time.sleep(0.5)
    img = PIL.ImageGrab.grab()
    #imgplot = plt.imshow(img)
    data=pytesseract.image_to_data(img)

    data=data.split()
    print(data)
    
    for i in range(len(data)):
        if ' '.join(text) in data[i].lower():
            print("Match Found")
            #coord_x = int(data[i-5]) + int(data[i-3]/2)
            #coord_y = int(data[i-4]) + int(data[i-2]/2)
            coord_x = int(data[i-5]) + int(int(data[i-3])/2)
            coord_y = int(data[i-4]) + int(int(data[i-2])/2)
            mouse.double_click(button="left",coords=(coord_x,coord_y))
            print("Double Clicked at: (" ,coord_x,",", coord_y,")")
            break
        
def user_right_click(text):
    time.sleep(0.5)
    img = PIL.ImageGrab.grab()
    #imgplot = plt.imshow(img)
    data=pytesseract.image_to_data(img)

    data=data.split()
    print(data)
    
    for i in range(len(data)):
        if ' '.join(text) in data[i].lower():
            print("Match Found")
            #coord_x = int(data[i-5]) + int(data[i-3]/2)
            #coord_y = int(data[i-4]) + int(data[i-2]/2)
            coord_x = int(data[i-5]) + int(int(data[i-3])/2)
            coord_y = int(data[i-4]) + int(int(data[i-2])/2)
            mouse.click(button="right",coords=(coord_x,coord_y))
            print("Right Clicked at: (" ,coord_x,",", coord_y,")")
            break
        
def keyboard_ip(text):
    for x in text:
        SendKeys(x)
        SendKeys("{VK_SPACE}")
        
def wait(text):
    for i in range(len(text)):
            if text[i]=='seconds' or text[1]=='second':
                wait_time = int(text[i-1])
                print("Waiting...")
                if(wait_time>5):
                    time.sleep(wait_time-5)

while True:
    winsound.Beep(frequency, duration)
    #time.sleep(1)
    query = str(speech.press_record())       #converting speech to text using speech_to_text API 
    #query=input("Enter Command (Type exit to quit): ")
    #time.sleep(3)
    if query.lower()=='exit' or query.lower()=='quit':
        break
    else:
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
    words=[word.text.lower() for word in doc if word.is_stop==False]
    words=list(words)
    #verbs, obj = words[0], ' '.join(words[1:])
    verbs, obj = words[0], words[1:]
    print(words)
    print("Verb: ", verbs, " Obj: ", obj)
    '''token=nlp("start")
    similarity_start = token.similarity(nlp(verbs))
    token=nlp("click")
    similarity_click = token.similarity(nlp(verbs))
    print("Similarity with \'start\': ", similarity_start)
    print("Similarity with \'click\': ", similarity_click)'''
    apps=[]
    #if float(similarity_start)>0.5:
    if verbs=='start' or verbs=='open' or verbs=='launch':
        for x in obj:
            start_app(x)
    #elif float(similarity_click)>0.5:
    elif verbs=='click':
        user_single_click(obj)
    elif verbs=="double" or verbs=='doubleclick':
        user_double_click(obj[1:])
    elif verbs=='right' or verbs=='rightclick':
        user_right_click(obj[1:])
    elif verbs=="type" or verbs=="write":
        keyboard_ip(obj)
    elif verbs=="go":
        if obj==["back"]:
            SendKeys("%{LEFT}")
        if obj==["forward"]:
            SendKeys("%{RIGHT}")
    elif verbs=="play" or verbs=="pause":
        SendKeys("{VK_SPACE}")
    elif verbs=="select" and obj==["all"]:
        SendKeys("^a")
    elif verbs=="copy":
        SendKeys("^c")
    elif verbs=="paste":
        SendKeys("^v")
    elif verbs=="cut":
        SendKeys("^x")
    elif verbs=="close":
        SendKeys("%{F4}")
    elif verbs=='wait':
        wait(obj)
    
    time.sleep(3)


#imge = Image.open(img)
'''data=pytesseract.image_to_data(img)

data=data.split()
print(data)

for i in range(len(data)):
    if "devalj" in data[i]:
        print("Match Found")
        #coord_x = int(data[i-5]) + int(data[i-3]/2)
        #coord_y = int(data[i-4]) + int(data[i-2]/2)
        coord_x = int(data[i-5]) + int(int(data[i-3])/2)
        coord_y = int(data[i-4]) + int(int(data[i-2])/2)
        mouse.click(button="left",coords=(coord_x,coord_y))
        print("Mouse Moved")
        break
        '''
        
