import speech_recognition as sr
import speech, time, winsound

frequency = 1000
duration = 1000

def nlp_file():
    import nlp

r=sr.Recognizer()
keyword='Scooby'
with sr.Microphone() as source:
    print('Start talking')
    while True:
        winsound.Beep(frequency, duration)
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if keyword.lower() in text.lower():
                print("\'Scooby\' Detected in speech")
            nlp_file()
        except Exception as e:
            print('speak again')
            time.sleep(1)
            continue