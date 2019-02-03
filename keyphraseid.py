import speech_recognition as sr
import speech
r=sr.Recognizer()
keyword='Scooby'
with sr.Microphone() as source:
    print('Start talking')
    while True:
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if keyword.lower() in text.lower():
                import nlp
        except Exception as e:
            print('speak again')