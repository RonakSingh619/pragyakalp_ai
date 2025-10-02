import socket
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def setAlarm(alarmTimeStr, speak):
    import winsound
    import time
    from datetime import datetime
    import re

    print(alarmTimeStr)
    pattern = r'\b(?:(?:[01]?\d|2[0-3])\s*[.:]\s*[0-5]\d(?::[0-5]\d)?\s?(?:[AaPp][Mm])?|\b(?:1[0-2]|0?[1-9])\s?[AaPp][Mm])\b'
    match = re.findall(pattern, alarmTimeStr.lower())

    try:
        Time = match[0].replace(" ", "").replace("am", "").replace("pm", "")
        print("res: ", match[0].replace(" ", "").replace("am", "").replace("pm", "").replace(".", ":"))
    except IndexError:
        print("No valid time found in the input.")
        return

    # def playAlarm():
    #     for _ in range(3):
    #         winsound.Beep(1000, 500)
    #         time.sleep(0.5)

    # try:
    #     alarmTime = datetime.strptime(Time, "%H:%M")
    #     print(f"Alarm set for {Time}")

    #     while True:
    #         current_time = datetime.now()
    #         alarm_datetime = current_time.replace(
    #             hour=alarmTime.hour,
    #             minute=alarmTime.minute,
    #             second=0,
    #             microsecond=0
    #         )

    #         if current_time >= alarm_datetime:
    #             print("Alarm ringing!")
    #             playAlarm()
    #             break

    #         time.sleep(1)
    # except ValueError:
    #     print("invalid time format!!")

def newsUpdate():
    pass

def openImage():
    pass

def generatePPT():
    pass

def play_youtube_song(song_name, speak):

    # Set up Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open YouTube
        driver.get("https://www.youtube.com")
        
        # Wait for page to load
        time.sleep(2)
        
        # Find search bar and enter song name
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys(song_name)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for search results to load
        time.sleep(3)
        
        # Find and click the first video result
        # Using XPATH to find the first video title link
        first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()
        
        # Keep the browser open to play the video
        # You can adjust the sleep time or remove it based on your needs
        driver.refresh()
        time.sleep(300)  # Keeps video playing for 5 minutes
        
    except Exception as e:
        print(f"An error occurred while playing music: {e}")
        
    finally:
        # Uncomment the line below if you want the browser to close after playing
        # driver.quit()
        pass

def isThisListInThisString(lists, str):
    for i in lists:
        if i in str:
            return True
    return False

def check_internet():
    hostname = "8.8.8.8"
    try:
        socket.create_connection( (hostname, 53), timeout=3 )
        # print("Connected to internet")
        return True
    except Exception as e:
        # print("Not connected to internet: ", e)
        return False