import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  
engine.setProperty('rate', 170)
engine.setProperty('volume',1)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    '''
    greets the user according to the time of the day
    '''
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning Akshat!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon Akshat!")
    elif hour >= 17 and hour < 20:
        speak("Good Evening Akshat!")
    else:
        speak("Good Evening Akshat!")

    speak("How may I help you?")

def takeComm():
    input=sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        print("Listening...")
        input.adjust_for_ambient_noise(source, duration = 1)
        input.energy_threshold = 700
        input.pause_threshold = 0.8 
        input.non_speaking_duration = 0.1
        audio=input.listen(source)

    try:
        print("Recognizing...")
        query = input.recognize_google(audio, language= "en-in")
        print(query)
    
    except Exception as e:
        print(e)
        print("Sorry, I couldn't understand you. Please say that again")
        return "None"
    return query


if __name__ == "__main__":
    greet()
    while True:
        query = takeComm().lower()
        if query == 0:
            continue

        if "stop" in str(query) or "exit" in str(query) or "bye" in str(query):
            speak("Ok bye and take care")
            break
        
        if "what is your name" == query:
            speak("my name is lalit")
        
        elif "how are you" == query:
            speak("i am fine")

        elif "kaun lalit" == query:
            sound_dir = "C:\\Users\\aksha\\Desktop\\lalitassistant\\soundfx"
            songs = os.listdir(sound_dir)
            print(songs)    
            os.startfile(os.path.join(sound_dir, songs[0]))
        
        elif "open steam" in query:
            steamPath = "C:\\Program Files (x86)\\Steam\\steam.exe"
            os.startfile(steamPath)

        elif "open discord" in query:
            discordPath = "C:\\Users\\aksha\\AppData\\Local\\Discord\\app.exe"
            os.startfile(discordPath)

        elif "open youtube" in query:
            webbrowser.get('brave').open("youtube.com")

        elif "open duckduckgo" in query:
            webbrowser.open("duckduckgo.com")

        elif 'what is the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
                   
        