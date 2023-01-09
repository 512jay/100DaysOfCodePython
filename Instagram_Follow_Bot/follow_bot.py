import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time


CHROME_DRIVER_PATH = "/Development/chromedriver"
SIMILAR_ACCOUNT = "thehightechrevolution"  # To be updated later
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:
    """A class for following Instagram followers from selected account."""

    def __init__(self, account: str):
        self.account_following = account
        # Create selenium driver
        self.service = Service(CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()
        time.sleep(5)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


follower = InstaFollower(SIMILAR_ACCOUNT)
