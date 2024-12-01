import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first available voice

def speak(audio):
    """Converts text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Wishes the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis, sir. Please tell me, how may I help you?")

def takeCommand():
    """
    Listens to the user's voice input and converts it to text.
    Returns 'None' if the input couldn't be understood.
    """
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')  # Using Google API for speech recognition
            print(f"User said: {query}\n")
        except Exception as e:
            print("Could not understand audio, please say that again...")
            return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            break
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google'in query:
            webbrowser.open("google.com")
        elif 'open chatgpt'in query:
            webbrowser.open("chatgpt.com")

        elif 'play music' in query:
            music_dir=''

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strtime}")
        elif 'open spotify' in query:
            codePath=""
