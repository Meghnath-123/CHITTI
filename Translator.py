from googletrans import Translator, LANGUAGES  # import LANGUAGES to display available options
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import os
from playsound import playsound
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(LANGUAGES)  # Display available languages
    translator = Translator()
    speak("Choose the language in which you want to translate")
    b = input("To_Lang :- ")
    
    try:
        text_to_translate = translator.translate(query, src="auto", dest=b)
        text = text_to_translate.text
        print(f"Translated text: {text}")
        
        speakgl = gTTS(text=text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        playsound("voice.mp3")
        
        time.sleep(5)
        os.remove("voice.mp3")
    except Exception as e:
        print("Unable to translate:", e)
