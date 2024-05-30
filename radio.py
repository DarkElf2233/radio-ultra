from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://radioultra.ru/")

radio = driver.find_element(By.CLASS_NAME, "player__current")
title = radio.find_element(By.CLASS_NAME, 'player__song').text
author = radio.find_element(By.CLASS_NAME, 'player__artist').text

with open('songs.txt', 'a') as file:
    file.write(f'{author} - {title}\r')

driver.close()
