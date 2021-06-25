from gtts import gTTS
import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import string

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You: " + data)
    except sr.UnknownValueError:
        print("I could not understand audio")
    return data

def webSearch():
    r5 = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("what website would you like me to search for you? ")
        audio = r5.listen(source)
        url5= r5.recognize_google(audio)
        if "search" in url5:
            no,url = url5.split()
        try:
            print("Google Speech Recognition thinks you said " + r5.recognize_google(audio))
            webbrowser.open_new("https://"+url+".com")                                                                        
        except sr.UnknownValueError:                                                                        
            print("Google Speech Recognition could not understand audio")                                                                        


def friday(data):
    if "how are you" in data:
        speak("I am fine")
    elif "WhatsApp" in data:
        speak("Nothing much")
    elif "what time is it" in data:
        speak(ctime())
    elif "are you up" in data:
        speak("Always for you Sr")
    elif "what's your name" in data:
        speak("My name is Friday")
    elif "Hello" in data:
        speak("Hello")
    elif "hi" in data:
        speak("Hello")
    elif "thank you" in data:
        speak("You're Welcome")
    elif "bye" in data:
        speak("Good bye Sr")
    elif "hello" and "search" in data:
        webSearch()
    elif "search" in data:
        webSearch()
        
    else:
        speak("Im sorry i dont understand that :(")


time.sleep(2)
speak("Friday: Hi Sr, what can I do for you?")
while True:
    data = recordAudio()
    friday(data)
    if "bye" in data:
        break
