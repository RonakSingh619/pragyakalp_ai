import os
from datetime import datetime
import sys
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyautogui
import Data.Credentials as Crd

Cred = Crd.Credentail()
# print("Cred: ",Cred)

def init_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    laundaVoice = voices[0].id
    laundiyaVoice = voices[1].id
    engine.setProperty('voice', laundaVoice)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    return engine

def speak(text):
    engine = init_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening..........", end="", flush=True)
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        audio = r.listen(source)
    try:
        print("\r", end="", flush=True)
        print("Processing............", end="", flush=True)
        query = r.recognize_google(audio, language='en-in')
        print("\r", end="", flush=True)
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please!: ",e)
        return "None"
    return query

def cal_day():
    day = datetime.today().weekday()+1
    dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if day in dict.keys():
        dayOfWeek = dict[day]
        # print(dayOfWeek)
    return dayOfWeek
def WishMe():
    hr = int(datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()
    if( (hr>=0) and (hr<=12) and ('AM' in t) ):
        speak(f"Good morning {Cred['userName']}, it's {day} and the time is {t}")
    elif( (hr>=12) and (hr<=16) and ('PM' in t) ):
        speak(f"Good afternoon {Cred['userName']}, it's {day} and the time is {t}")
    else:
        speak(f"Good evening {Cred['userName']}, it's {day} and the time is {t}")

def SocailMedia(command):
    if( 'facebook' in command ):
        speak("Opening your facebook account")
        webbrowser.open("https://www.facebook.com/")
    elif( 'whatsapp' in command ):
        speak("Opening your whatsapp account")
        webbrowser.open("https://www.whatsapp.com/")
    elif( 'discord' in command ):
        speak("Opening your discord account")
        webbrowser.open("https://www.discord.com/")
    elif( 'instagram' or 'insta' in command ):
        speak("Opening your instagram account")
        webbrowser.open("https://www.instagram.com/")

def Schedule():
    day = cal_day().lower().capitalize()
    week = {
        "Monday": "On Monday, you are going college",
        "Tuesday": "On Tuesday, you will be playing outlast 2",
        "Wednesday": "On Wednesday, you will be playing Max Payne 2",
        "Thursday": "On Thursday, you are supposed work on me",
        "Friday": "On Friday, you are going gym",
        "Saturday": "On Saturday, you are supposed to hang out with your friends",
        "Sunday": "On Sunday, you are supposed to rest"
    }
    if day in week.keys():
        speak(week[day])

def HandelVolumes(command):
    if( ("volume up" in command) or ("increase volume" in command) ):
        pyautogui.press("volumeup")
        speak("Volume increased")
    elif( ("volume down" in command) or ("decrease volume" in command) ):
        pyautogui.press("volumedown")
        speak("Volume decreased")
    elif( "mute" in command ):
        pyautogui.press("volumemute")
        speak("Volume muted")

def OpenApp(command):
    if("open calculator" in command):
        speak("Opening calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    elif("open notepad" in command):
        speak("Opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")
    elif("open excel" in command):
        speak("Opening excel")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    elif("open chrome" in command):
        speak("Opening chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

def CloseApp(command):
    if("close calculator" in command):
        speak("closing calculator")
        os.system("taskkill /f /im calc.exe")
    elif("close notepad" in command):
        speak("closing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif("close excel" in command):
        speak("closing excel")
        os.system("taskkill /f /im EXCEL.EXE")
    elif("close chrome" in command):
        speak("closing chrome")
        os.system("taskkill /f /im chrome.exe")

# speak("Good afternoon sir, how can i assist you today?")

if __name__ == "__main__":
    WishMe()
    while True:
        q = command().lower()
        # q = input("Enter your command: ")
        if( ('facebook' in q) or ('whatsapp' in q) or ('discord' in q) or ('instagram' in q) ):
            print(q)
            SocailMedia(q)
        elif( ('time table' in q) or ('schedule' in q) ):
            Schedule()
        elif( ("volume up" in q) or ("increase volume" in q) or ("volume down" in q) or ("decrease volume" in q) or ("mute" in q) ):
            HandelVolumes(q)
        elif( ("open calculator" in q) or ("open notepad" in q) or ("open excel" in q) or ("open chrome" in q) ):
            OpenApp(q)
        elif( ("close calculator" in q) or ("close notepad" in q) or ("close excel" in q) or ("close chrome" in q) ):
            CloseApp(q)
        elif( "exit" in q ):
            sys.exit()

# speak("bokachoda")
# speak("toddi penn di phooddi")