import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import random
import os

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak('Good night')
    speak('Welcome Mr. Kunal')
    speak("I am Jarvis the Robot. How Can I help You.I am developed by Mr. Kunal Yadav")

def take_command():
    # it will take microphne input from the user and convert speech to string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please")

        return "None"
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query=take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open gmail.com" in query:
            webbrowser.open("gmail.com")
        elif "play music" in query:
            music_dir='E:\\videos\\music videos'
            songs=os.listdir(music_dir)
            k=random.randint(1,20)
            os.startfile(os.path.join(music_dir,songs[k]))
        elif "the time " in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")





