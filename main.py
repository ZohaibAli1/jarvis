import pyttsx3
import speech_recognition as sr
from googletrans import Translator

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
new_rate = rate - 25
engine.setProperty('rate', new_rate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ur-PK')
        translation = Translator().translate(query, src='ur', dest='en')
        print(f"You Said: {translation.text}")
        return query
    except Exception as e:
        print("Please Speak Again..")
        speak("Please Speak Again..")
        return takecommand()
takecommand()

