"""IMPORTANT NOTE: 
It seems that Linkedin gives a lot of trouble to scrapers.
I created a fake account with a fake email adress, but I got instantly blocked. 
Because I don't want to use my main account to scrap data, risking restrictions, 
I drop this phase for now."""

import time
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

LINKEDIN_PWD = os.getenv("LINKEDIN_PWD")
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
# CHROME_PATH
HOME = Path.home()

## Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

# Creating a webdriver instance
driver = webdriver.Chrome(HOME / "chromedriver/stable/chromedriver", chrome_options=chrome_options)
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

# Login
# entering username
username = driver.find_element(by=By.ID, value="username")
username.send_keys(LINKEDIN_EMAIL)
# entering password
pword = driver.find_element(by=By.ID, value="password")
pword.send_keys(LINKEDIN_PWD)	
# Clicking on the log in button
driver.find_element(by=By.XPATH, value="//*[@type='submit']").click()

driver.quit()
