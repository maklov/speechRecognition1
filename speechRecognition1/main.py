import speech_recognition as sr
from os import path
import sys
import pyaudio

# os.path.join(path.abspath('C:\\Users\\yaneq\\PycharmProjects'))

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Record a message: ')
    audio = recognizer.listen(source)

words = recognizer.recognize_google(audio)

if 'Hello' in words:
    print('Hello to you too!')
if 'are you a computer' in words:
    print('Yes, I\'m a computer')
# if 'run snake' in words:


# duration = audio.sample_width()

file = open('speech2txt.txt','w')
print(words)
file.write(words)
