import os
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


CHROME_DRIVER_PATH = "/Development/chromedriver"
SIMILAR_ACCOUNT = "thehightechrevolution"  # To be updated later
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


def find_button_text_index(buttons, text) -> int:
    index = 0
    for button in buttons:
        if button.text == text:
            return index
        else:
            index += 1


class InstaFollower:
    """A class for following Instagram followers from selected account."""

    def __init__(self, account: str):
        self.account_following = account
        # Create selenium driver
        self.service = Service(CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()

    def login(self):
        """Log in to Instagram and clear popups"""

        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)
        # select inputs
        inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        inputs[0].send_keys(USERNAME)
        inputs[1].send_keys(PASSWORD)

        # Click "Log in" button
        time.sleep(5)
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        buttons[find_button_text_index(buttons, "Log in")].click()

        # Click "Not Now" button to saving login info
        time.sleep(10)
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        buttons[find_button_text_index(buttons, "Not Now")].click()

        # Click "Not Now" to Notifications
        time.sleep(5)
        buttons = self.driver.find_elements(by=By.TAG_NAME, value="button")
        buttons[find_button_text_index(buttons, "Not Now")].click()

        time.sleep(30)

    def find_followers(self):
        pass

    def follow(self):
        pass

    def quit(self):
        self.driver.quit()


bot = InstaFollower(SIMILAR_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
