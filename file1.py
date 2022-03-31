import pyttsx3
import datetime


engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
newVoiceRate = 150 
engine.setProperty('rate', newVoiceRate)
engine.say("Hello Kaartik, This is Pondi")
engine.runAndWait()

engine.say("Let's get Started")
engine.say("Do you want me to rep you up through your day")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("this is PONDI")

