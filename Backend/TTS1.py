from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import chromedriver_autoinstaller
from chromedriver_autoinstaller import install

chrome_path = install()

chrome_options=Options()

service= Service(executable_path=chrome_path)

driver=webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://readloud.net/english/british/1-male-voice-brian.html")

script = """function mediaElementIsPlaying(el) {
  return el && el.currentTime > 0 && !el.paused && !el.ended && el.readyState > 2;
}

// Check if any audio element is playing
const audioIsPlaying = !![...document.getElementsByTagName('audio')].find((el) => mediaElementIsPlaying(el));

// If either audio or video is playing, return true
return audioIsPlaying;"""

def TextToSpeech(text):
  try:
    textarea =  driver.find_element(By.NAME, "but1")
    textarea.clear()
    textarea.send_keys(text)

    submit= driver.find_element(By.NAME, "butt0")
    submit.click()

    while 1:
     playing=driver.execute_script(script)
     if not playing:
        break  
     sleep(0.1)

  except Exception as e:
    print(e)
    print("Restarting website")
    driver.get("https://readloud.net/english/british/1-male-voice-brian.html")
    TextToSpeech(text)

if __name__ == "__main__":
    while 1:
       driver.save_screenshot("screen.png")
       text= input(">>>   ")
       TextToSpeech(text)

#input("press enter to exit....")