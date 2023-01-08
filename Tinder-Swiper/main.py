from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/Development/chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)
url = "https://www.tinder.com"
driver.get(url)
login = driver.find_element(by=By.LINK_TEXT, value="Log in")
time.sleep(2)
login.click()
time .sleep(500)
print("I'm in.")
driver.quit()
