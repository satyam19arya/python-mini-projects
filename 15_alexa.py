import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
from playsound import playsound
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("Good Morning! sir")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!sir")
    elif hour>=0 and hour<7:
        speak("Good Evening!sir")
    else:
        speak("Hello sir!")

    speak("I am your assistant. Please tell me how may I help you")      


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')

        elif 'open whatsapp' in query:
            webbrowser.open('https://web.whatsapp.com/')

        elif 'open sex' in query:
            webbrowser.open('https://www.sexvid.pro/')

        elif 'open x' in query:
            webbrowser.open('https://www.sexvid.pro/')

        elif 'open vs code' in query:
            codePath ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open spotify' in query:
            codePath="C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)
    
        elif 'play music' in query:
            playsound('song.mp3')

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime('%H-%M-%S')
            speak(f"Sir,the time is {strTime}")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'bye bye' in query:
            print("Thank you sir! Have a great day")
            speak("Thank you sir! Have a great day")
            exit()