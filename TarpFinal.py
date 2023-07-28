# import speech_recognition as sr
# import pyttsx3
# from playsound import playsound

# # initialize speech recognition and text-to-speech engines
# r = sr.Recognizer()
# engine = pyttsx3.init()

# # define the trigger words
# trigger_words = ["help", "save", "run", "emergency", "disaster", "bachhao", "bachao"]

# # define a function to handle recognized speech
# def handle_speech(phrase):
#     print("You said: " + phrase)
#     if any(word in phrase for word in trigger_words):
#         print("Alert: Trigger word detected!")
#         playsound("alert.wav")  # play sound alert
#         engine.say("Alert: Trigger word detected!")
#         engine.runAndWait()

# # listen to the microphone and recognize speech
# with sr.Microphone() as source:
#     print("Speak now...")
#     while True:
#         try:
#             audio = r.listen(source)
#             phrase = r.recognize_google(audio)
#             handle_speech(phrase)
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))

import speech_recognition as sr
import pyttsx3
from playsound import playsound

# initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# define the trigger words and stop words
trigger_words = ["help", "save", "Run", "emergency", "disaster", "Bachao"]
stop_words = ["stop sound", "shutdown"]

# define a function to handle recognized speech
def handle_speech(phrase):
    print("You said: " + phrase)
    if any(word in phrase for word in trigger_words):
        print("Alert: Trigger word detected!")
        playsound("alert.wav")  # play sound alert
        engine.say("Alert: Trigger word detected!")
        engine.runAndWait()
    elif any(word in phrase for word in stop_words):
        print("Stop command detected!")
        playsound(None)  # stop sound alert

# listen to the microphone and recognize speech
with sr.Microphone() as source:
    print("Speak now...")
    while True:
        try:
            audio = r.listen(source)
            phrase = r.recognize_google(audio)
            handle_speech(phrase)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
            
#ijngjfnh mjfnv jhfkmpfg kfuhd td @RCb bhu'
#Kjnfngj huifhifm nhhi jijfrrjjrjr oprkogmjk jkvnivb
#jhfbun fhvf jnh(Fbm):frj      
            
            
            
            