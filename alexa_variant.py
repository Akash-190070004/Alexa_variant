# these are some modules needed for this project
import pywhatkit

# this is for recognizing speech
import speech_recognition as sr

# this pyttsx3 module is to convert text (in string format) into speech(alexa will say that text for you
import pyttsx3 as pyt

# this module for getting date and time
import datetime

# this module for knowing information (in summary) of anything from wikipedia
import wikipedia as wiki

# this one for listening a joke by alexa
import pyjokes

# this is to make python sleep for some seconds by using time.sleep(seconds)
import time

# to exit the code when you say thank you
import sys

"""this engine code we first initialized pyt module and then female voice for alexa               """
engine = pyt.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

"""here  we defined a talk function that will say some text when called with some text """


def talk(text):
    engine.say(text)
    engine.runAndWait()


# here we are kinda initialising the sr module

listener = sr.Recognizer()


# here we are getting the command in text of what we said to alexa


def get_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            time.sleep(1)
            voice = listener.listen(source)
            # using google api to convert speech into text
            command = listener.recognize_google(voice)
            command = command.lower()
            # we don't want to use alexa in our final command

            command = command.replace("alexa", "")
        return command

        # in case  command is vague or can't be scrutinised then ..

    except:
        return " say something in english sir "


# here magic of alexa starts

def run_alexa():
    command = get_command()

    # to play something on youtube (literally anything!!!)

    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song + "on Youtube")
        print("playing " + song + " on Youtube")
        pywhatkit.playonyt(song)

    # to get current time

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")

        print(" current time is " + time)
        talk(" current time is " + time)

    # to get summary from wikipedia

    elif " what is " in command:
        thing = command.replace("what is ", "")
        info = wiki.summary(thing, 1)
        print(info)
        talk(info)
    elif " who is " in command:
        thing = command.replace("who is ", "")
        info = wiki.summary(thing, 1)
        print(info)
        talk(info)

    # to listen to a joke by alexa

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "thank you " in command:
        print(" good night  sir,  have a nice day , see you again ")
        talk(" good night sir ,have a nice day , see you again ")
        sys.exit()



    else:

        print("can't get you say something again")
        talk("can't get you say something again")


# running alexa for you infinitely

while True:
    run_alexa()
