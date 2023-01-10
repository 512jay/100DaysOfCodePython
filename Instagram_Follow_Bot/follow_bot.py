import os
import time
from random import choice
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/Development/chromedriver"
SIMILAR_ACCOUNT = "thehightechrevolution"  # To be updated later
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


def wait():
    random_times = [5, 6, 7, 8, 9]
    time.sleep(choice(random_times))


class InstaFollower:
    """A class for following Instagram followers from selected account."""

    def __init__(self, account: str):
        self.account_following = account
        # Create selenium driver
        self.service = Service(CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()

    def click_tag_with_text(self, tag: str, text: str):
        index = 0
        buttons = self.driver.find_elements(by=By.TAG_NAME, value=tag)
        # print("\n*******")
        for button in buttons:
            # print(f"{index}: {button.text}")
            if text in button.text:
                wait()
                buttons[index].click()
                break
            else:
                index += 1

    def scroll(self):
        wait()
        scrollable = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div["
                                                                 "1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)

    def login(self):
        """Log in to Instagram and clear popups"""

        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        wait()
        # select inputs
        inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        inputs[0].send_keys(USERNAME)
        inputs[1].send_keys(PASSWORD)
        # Click "Log in" button
        self.click_tag_with_text("button", "Log in")
        # Click "Not Now" button to saving login info
        # self.click_tag_with_text("button", "Not Now")
        # Click "Not Now" to Notifications
        self.click_tag_with_text("button", "Not Now")
        wait()

    def find_followers(self):
        url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"
        self.driver.get(url)
        wait()
        self.click_tag_with_text("li", "followers")
        # scroll through followers.
        # self.click_tag_with_text("div", "_aano")
        # Select active element
        # wait()
        # followers_window = self.driver.find_element(by=By.XPATH,
        # # value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[
        # 2]')
        # # /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]
        for i in range(5):
            self.scroll()

        time.sleep(600)

    def follow(self):
        pass

    def quit(self):
        self.driver.quit()
        print("End of Code!")


bot = InstaFollower(SIMILAR_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow()
bot.quit()
