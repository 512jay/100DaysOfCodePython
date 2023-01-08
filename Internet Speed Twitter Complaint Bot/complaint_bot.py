import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 200
PROMISED_UP = 100
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")


class InternetSpeedTwitterBot:
    """A class for connecting to selenium"""
    def __init__(self):
        self.service = Service('/Development/chromedriver')
        self.service.start()
        url = "https://twitter.com"
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.get(url)
        time.sleep(5)

    def quit(self):
        self.driver.quit()


complaint_bot = InternetSpeedTwitterBot()
complaint_bot.quit()
