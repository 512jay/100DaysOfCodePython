import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 200
PROMISED_UP = 100
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
TWITTER_EMAIL = os.environ.get("EMAIL")
TWITTER_PASSWORD = os.environ.get("PASSWORD")
TWITTER_HANDLE = os.environ.get("TWITTER_HANDLE")


class InternetSpeedTwitterBot:
    """A class for connecting to selenium"""
    def __init__(self):
        self.down = 0
        self.up = 0
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
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        time.sleep(5)

    def tweet_at_provider(self):
        url = "https://twitter.com"
        self.driver.get(url)
        time.sleep(5)
        login = self.driver.find_element(by=By.LINK_TEXT, value="Log in")
        login.click()
        time.sleep(5)
        input_email = self.driver.find_element(by=By.TAG_NAME, value="input")
        input_email.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        # May not need depending upon twitter login format
        twitter_name = self.driver.find_element(by=By.TAG_NAME, value="input")
        twitter_name.send_keys(os.environ.get("TWITTER_HANDLE"), Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_elements(by=By.TAG_NAME, value="input")
        password[1].send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(10)
        tweet_button = self.driver.find_element(by=By.LINK_TEXT, value="Tweet")
        tweet_button.click()
        time.sleep(5)
        active = self.driver.switch_to.active_element
        active.send_keys(f"Download speed was {self.down} Mps and upload was {self.up} Mps.")
        time.sleep(20)

    def quit(self):
        self.driver.quit()


complaint_bot = InternetSpeedTwitterBot()
complaint_bot.get_internet_speed()
complaint_bot.tweet_at_provider()
complaint_bot.quit()
