#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().system('pip install SpeechRecognition')


# In[2]:


import spacy
import speech_recognition as sr
import speech_recog


# In[12]:


nlp=spacy.load('en') 


# In[22]:


query = str('start mozilla')       #converting speech to text using speech_to_text API 

doc=nlp(query)

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
words=[word for word in doc if word.is_stop==False]


# In[35]:


# token=nlp('start the notepad')
# for i in token:
#     print(i.text,'-----',i.pos_)
# i_words=[word for word in token if word.is_stop==False]
# i_words


# In[36]:


# noun(i_words)


# In[34]:


query = str(speech_recog.press_record())       #converting speech to text using speech_to_text API 

print(query) 


# In[ ]:




