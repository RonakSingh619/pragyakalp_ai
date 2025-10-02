from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def play_youtube_song():
    # Get song name from user
    song_name = input("Enter the song name: ")
    
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
        print(f"An error occurred: {e}")
        
    finally:
        # Uncomment the line below if you want the browser to close after playing
        # driver.quit()
        pass

if __name__ == "__main__":
    play_youtube_song()