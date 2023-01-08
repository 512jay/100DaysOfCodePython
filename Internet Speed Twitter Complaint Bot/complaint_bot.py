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
        self.down = None
        self.up = None
        self.service = Service('/Development/chromedriver')
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"
        # class start-text
        self.driver.get(url)
        start_test = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        time.sleep(15)
        start_test.click()
        time.sleep(40)
        down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        print(down)
        print(up)

    def tweet_at_provider(self):
        url = "https://twitter.com/i/flow/login"
        self.driver.get(url)
        # login = self.driver.find_element(by=By.LINK_TEXT, value="Log in")
        # login.click()
        time.sleep(5)
        google = self.driver.find_element(by=By.TAG_NAME, value="iframe")
        google.click()
        time.sleep(60)

    def quit(self):
        self.driver.quit()


complaint_bot = InternetSpeedTwitterBot()
# complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider()
complaint_bot.quit()
