import json
from datetime import datetime
import sys
import time

from colorama import Fore
import psutil
# import Data.Credentials as Crd

# -------------------------------------  ---------------------------------------------



# ------------------------------------- Color for print() outputs ---------------------------------------------
# print(Fore.MAGENTA + "Say hey butler to initiate")
# with open("C:\\Ronak\\MCA\\2nd SEM\\Project\\AI Butler Project\\Data\\SocialMediaAcc.json", 'r') as f:
#     obj = json.load(f)
#     print(obj["Insta"]["password"])
    # print(f)

# def isIn(lists, str):
#     for i in lists:
#         if i in str:
#             return True
#     return False

words = input("Enter command: ")
print(isIn([ "message", "bund" ], words))

# ----------------------------------------------------------------------------------
# Cred = Crd.Credentail()

# def cal_day():
#     day = datetime.today().weekday()+1
#     dict = {
#         1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday",
#         4: "Thursday",
#         5: "Friday",
#         6: "Saturday",
#         7: "Sunday"
#     }
#     if day in dict.keys():
#         dayOfWeek = dict[day]
#         # print(dayOfWeek)
#     return dayOfWeek
# def GetDateAndTime():
#     hr = int(datetime.now().hour)
#     t = time.strftime("%I:%M:%p")
#     day = cal_day()
#     return f"it's {day} and the time is {t}"

# with open("C:\\Ronak\\MCA\\2nd SEM\\Python\\AI\\First AI\\intents.json") as file:
#     data = json.load(file)
#     print(type(data))

# intents_dic = dict(data)

# for obj in intents_dic['intents']:
#     if obj['tag'] == "datetime":
#         obj['responses'][0] = GetDateAndTime()
#         # print(obj)

# print((json.dumps(intents_dic)))

# ------------------------------------- Battery test ---------------------------------------------

# print(str(psutil.sensors_battery().percent))

# ------------------------------------- Wifi, etc On/Off program ---------------------------------------------
#---------- FAILURE ⚠️----------

# import subprocess
# import platform

# def toggle_wifi(enable: bool):
#     system = platform.system()
#     # print(system)
#     try:
#         if system.lower() == "windows":
#             if enable:
#                 subprocess.run([ "netsh", "interface", "set", "interface", "Wi-Fi", "enabled" ])
#     except Exception as e:
#         print("Error occured: ", e)

# toggle_wifi(True)

#---------- FAILURE ⚠️----------

# import os
# import platform

# def toggle_wifi(enable: bool):
#     system = platform.system()
#     # print(system)
#     try:
#         if system.lower() == "windows":
#             if enable:
#                 os.system("netsh interface set interface \"Wi-Fi\" enabled")
#     except Exception as e:
#         print("Error occured: ", e)

# toggle_wifi(True)

# ------------------------------------- Check internet connection ---------------------------------------------
# import socket

# def check_internet():
#     hostname = "8.8.8.8"

#     try:
#         socket.create_connection( (hostname, 53), timeout=3 )
#         print("Connected to internet")
#         return True
#     except Exception as e:
#         print("Not connected to internet: ", e)
#         return False

# ------------------------------------- Say something ---------------------------------------------
# comm = "say bund di lassi"
# s = str(comm).split(" ")
# str = " ".join(s[1:])
# print(str)

# ------------------------------------- Say hi to ---------------------------------------------
# str = "this is my friend samuel jackson"
# li = str.split(" ")
# index =  li.index("friend") + 1
# str2 = li[index]
# print("Hello " + str2)

# ------------------------------------- Offline speech recognition ---------------------------------------------

# import os
# import sounddevice as sd
# import numpy as np
# import vosk
# import json

# # Set the path for the Vosk model (adjust the path based on where you unzipped it)
# model_path = "C:\\Users\\ronak\\Downloads\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15"  # Adjust this path

# # Check if the model exists
# if not os.path.exists(model_path):
#     print(f"Please check the path to the model. The model directory should be: {model_path}")
#     exit(1)

# # Load the Vosk model
# model = vosk.Model(model_path)

# # Set up parameters for audio capture
# samplerate = 16000  # Sample rate of the microphone
# device = None  # Default microphone
# channels = 1  # Mono audio
# dtype = np.int16  # Audio data type

# # Create the recognizer instance
# rec = vosk.KaldiRecognizer(model, samplerate)

# # Define the callback function to process the audio input
# def callback(indata, frames, time, status):
#     if status:
#         print(status, file=sys.stderr)
#     # Convert the audio to the correct format for Vosk
#     audio_data = indata[:, 0]
#     rec.AcceptWaveform(audio_data.tobytes())

# # Start capturing audio and performing speech recognition
# with sd.InputStream(samplerate=samplerate, channels=channels, dtype=dtype, callback=callback):
#     print("Listening... (Press Ctrl+C to stop)")
#     while True:
#         # Poll for results
#         result = rec.Result()
#         if result:
#             result_json = json.loads(result)
#             if 'text' in result_json:
#                 print("Recognized: ", result_json)