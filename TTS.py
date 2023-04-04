# import os
# os.system("say 'this is a test of text to audio'") #mac os proprietary text to speech

import pyttsx3
from pyttsx3.voice import Voice

class TTS:
    def __init__(self):
        pass
    def tts(input):
        engine =pyttsx3.init()

        rate = engine.getProperty('rate')   # getting details of current speaking rate
        print (rate)                        #printing current  rate
        engine.setProperty('rate', 175) 
        engine.say(input)
        engine.runAndWait()


