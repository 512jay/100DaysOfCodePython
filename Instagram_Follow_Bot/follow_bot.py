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


class InstaFollower:
    """A class for following Instagram followers from selected account."""

    def __init__(self, account: str):
        self.account_following = account
        # Create selenium driver
        self.service = Service(CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()

    def click_tag_with_text(self, value: str, text: str):
        index = 0
        buttons = self.driver.find_elements(by=By.TAG_NAME, value=value)
        print("\n*******")
        for button in buttons:
            print(f"{index}: {button.text}")
            if text in button.text:
                buttons[index].click()
                break
            else:
                index += 1

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
        self.click_tag_with_text("button", "Log in")

        # Click "Not Now" button to saving login info
        time.sleep(10)
        self.click_tag_with_text("button", "Not Now")

        # Click "Not Now" to Notifications
        time.sleep(5)
        self.click_tag_with_text("button", "Not Now")
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(url)
        time.sleep(5)
        self.click_tag_with_text("li", "followers")
        print("End of code!")
        time.sleep(600)

    def follow(self):
        pass

    def quit(self):
        self.driver.quit()


bot = InstaFollower(SIMILAR_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
