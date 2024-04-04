"""
Hey there! I'm Sameer, and I'm excited to introduce you to my latest project: "Alexa" a Custom virtual assistant made with python.
1. Powered by {speech_recognition ,pyttsx3,pywhatkit,wikipedia,pyjokes}
2. Purpose: It listens to the microphone input, recognizes speech, and processes commands.
3. Interaction: The virtual assistant interacts with the user through voice responses using the pyttsx3 library.
4.User-Friendly Experience.

"""


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener= sr.Recognizer()
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command= command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                # print(command)    

    except:
        pass
    return  command


def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('Playing' + song)
        print('--> Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        # time=datetime.datetime.now().strftime('%H:%M %p')
        print('--> Current time is' + time)
        talk('Current time is' + time)
    elif 'wiki' in command:
        result=command.replace('wiki','')
        info=wikipedia.summary(result,2)#2 lines
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry dear!! My schedules tighter than a pair of skinny jeans')
    elif 'are you single' in command:
        talk('Single? oh, I am in a committed relationship with the wifi next door')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("Apologies, I didn't get that. Can you please repeat your request")


while True:
    run_alexa()