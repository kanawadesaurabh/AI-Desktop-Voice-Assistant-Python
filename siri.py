import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good aftrnoon!")

    else:
        speak("Good Evening!")

    speak("I am Siri sir. please tell me how may i help you")


def takeCommand():
    # it is microphone input from the user and return string output 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recogniziong...")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again Please...")
        return "None"
    return query


def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kanawadesaurabh1099@gmail.com', password)
    server.sendmail('kanawadesaurabh1099@gmail.com', to, content)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
   
        # Logic for executing takes on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open bootstrap' in query:
            webbrowser.open("bootstrap.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open bootstrap' in query:
            webbrowser.open("flipcart.com")

        elif 'play music' in query:
            music_dir = 'F:\songs\download'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%H")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath ="C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to saurabh' in quary:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kanawadesaurabh1099@gmail.com"
                sendEmail(to, content) 
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my frind saurabh I am not able to send this email!")