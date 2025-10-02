import winsound
import time
from datetime import datetime

# def playAlarm():
#     for _ in range(3):
#         winsound.Beep(1000, 500)
#         time.sleep(0.5)

# def setAlarm(alarmTimeStr):
#     try:
#         alarmTime = datetime.strptime(alarmTimeStr, "%H:%M")
#         print(f"Alarm set for {alarmTimeStr}")

#         while True:
#             current_time = datetime.now()
#             alarm_datetime = current_time.replace(
#                 hour=alarmTime.hour,
#                 minute=alarmTime.minute,
#                 second=0,
#                 microsecond=0
#             )

#             if current_time >= alarm_datetime:
#                 print("Alarm ringing!")
#                 playAlarm()
#                 break

#             time.sleep(1)
#     except ValueError:
#         print("invalid time format!!")

# setAlarm("11:17")

# -------------- Understanding alarm i/p --------------

import re

inp = "can u set alarm for 2.09 am"

pattern = r'\b(?:(?:[01]?\d|2[0-3])\s*[.:]\s*[0-5]\d(?::[0-5]\d)?\s?(?:[AaPp][Mm])?|\b(?:1[0-2]|0?[1-9])\s?[AaPp][Mm])\b'
match = re.findall(pattern, inp.lower())

print("res: ", match[0].replace(" ", "").replace("am", "").replace("pm", "").replace(".", ":"))