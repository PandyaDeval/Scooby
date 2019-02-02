import spacy 
import speech_recognition as sr
import speech
# nlp=spacy.load('en') 
# query = str('start mozilla')       #converting speech to text using speech_to_text API 
# doc=nlp(query)

# def noun(x):
#     nounlist=[]
#     for token in x:
#         if token.pos_=='NOUN':
#             nounlist.append(token.text)
#     return nounlist

# def adj(x):
#     adjlist=[]
#     for token in x:
#         if token.pos_=='ADJ':
#             adjlist.append(token.text)
#     return adjlist
# def verb(x):
#     verblist=[]
#     for token in x:
#         if token.pos_=='VERB':
#             verblist.append(token.text)
#     return verblist

# if not noun(doc):
#     pass
# else:
#     name=noun(doc)[0]

# if not adj(doc):
#     pass
# else:
#     task=adj(doc)[0]
    
# if not verb(doc):
#     pass
# else:
#     do=verb(doc)[0]

# from spacy.lang.en.stop_words import STOP_WORDS
# words=[word for word in doc if word.is_stop==False]




query = str(speech.press_record())       #converting speech to text using speech_to_text API 

print(query) 