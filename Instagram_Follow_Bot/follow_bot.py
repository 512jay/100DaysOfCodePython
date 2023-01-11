import os
import time
from random import choice
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "/Development/chromedriver"
SIMILAR_ACCOUNT = "high.tech.products"  # Use whatever account you want here
# Using this code, I would appreciate a follow on the gram. https://www.instagram.com/DevCroesus/
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


def wait():
    """Generates a random wait time."""
    random_times = [15, 20, 17, 15, 19]
    time.sleep(choice(random_times))


class InstaFollower:
    """A class for following Instagram followers from selected account."""

    def __init__(self, account: str):
        self.account_following = account
        self.follower_count = 0
        # Create selenium driver
        self.service = Service(CHROME_DRIVER_PATH)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)
        self.driver.maximize_window()

    def click_tag_with_text_in(self, tag: str, text: str):
        """Clicks on the tag which has the given text in it, if text is not found it does nothing."""
        wait()
        index = 0
        tags = self.driver.find_elements(by=By.TAG_NAME, value=tag)
        wait()
        for tag in tags:
            if text in tag.text:
                wait()
                tags[index].click()
                break
            else:
                index += 1

    def click_tag_exact(self, tag: str, text: str):
        index = 0
        tags = self.driver.find_elements(by=By.TAG_NAME, value=tag)
        wait()
        for tag in tags:
            if text == tag.text:
                wait()
                tags[index].click()
                return
            else:
                index += 1
        # print(f'<{tag}> Tag does not exist with exact string "{text}"')
        return -1

    def scroll_followers(self):
        """Scrolls down the followers."""

        wait()
        # uncomment to use the xpath method
        # scrollable = self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div[2]/div/div/div["
        #                                                          "1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        scrollable = self.driver.find_element(by=By.CLASS_NAME, value="_aano")
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable)

    def login(self):
        """Log in to Instagram and clear popups."""

        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        wait()
        # select inputs
        inputs = self.driver.find_elements(by=By.TAG_NAME, value="input")
        inputs[0].send_keys(USERNAME)
        inputs[1].send_keys(PASSWORD)
        # Click "Log in" button
        self.click_tag_with_text_in("button", "Log in")
        # Click "Not Now" button to saving login info
        self.click_tag_with_text_in("button", "Not Now")
        # Click "Not Now" to Notifications
        self.click_tag_with_text_in("button", "Not Now")
        wait()

    def find_followers(self):
        """Clicks on the followers for the target account."""

        url = f"https://www.instagram.com/{self.account_following}/"
        self.driver.get(url)
        wait()
        # Follow the account
        self.click_tag_exact("button", "Follow")
        # Get follower count
        list_items = self.driver.find_elements(by=By.TAG_NAME, value="li")
        self.follower_count = int(list_items[1].text.split(' ')[0])
        print(f"{SIMILAR_ACCOUNT} has {self.follower_count} followers")
        wait()

    def follow_followers(self):
        """Follow the followers."""
        self.click_tag_with_text_in("li", "followers")
        wait()
        for i in range(self.follower_count):
            print(f"Round ({i})")
            if self.click_tag_exact("button", "Follow") == -1:
                print("Checking for cancel button")
                if self.click_tag_exact("button", "Cancel") == -1:
                    print("Scrolling!")
                    self.scroll_followers()

    def quit(self):
        """Provides a clean exit with some time for discovery"""

        time.sleep(60)  # A time delay for analyzing code.
        self.driver.quit()
        print("End of Code!")


bot = InstaFollower(SIMILAR_ACCOUNT)
bot.login()
bot.find_followers()
bot.follow_followers()
bot.quit()
