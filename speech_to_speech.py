import pytesseract	 
import pyttsx3		 
import googletrans
from googletrans import Translator	
import numpy as np
import pyaudio
import speech_recognition as sr
import webbrowser as wb
# print(googletrans.LANGUAGES)

rec1 = sr.Recognizer()
rec2 = sr.Recognizer()
rec3 = sr.Recognizer()

while True:
    # Audio input 
    with sr.Microphone() as source:
        print("listening...")
        audio = rec1.listen(source)

    try:
        audio_text = rec2.recognize_google(audio)
        if (audio_text == 'exit'):
            break
        print("scr_text:", audio_text)

    except sr.UnknownValueError:
        print("error")

    except sr.RequestError:
        print("error")
    		
    # Translate extracted text to destination language 
    p = Translator()
    k = p.translate(audio_text,dest='french')	 # german , french
    print("dest_text:",k.text)
    del audio_text


    # Text to speech 
    engine = pyttsx3.init() 
    engine.say(k.text)							 
    engine.runAndWait() 
