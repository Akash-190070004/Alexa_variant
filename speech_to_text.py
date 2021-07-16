import speech_recognition as sr
import time

listener = sr.Recognizer()

# it will ensure that the person gets only 4 chances
for i in range(1, 5):
    try:

        with sr.Microphone() as source:
            print("listening...")
            time.sleep(1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
