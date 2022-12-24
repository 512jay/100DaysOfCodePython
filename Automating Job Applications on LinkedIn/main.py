from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
email = os.environ.get('email')
password = os.environ.get('password')

service = Service('/Development/chromedriver')

service.start()

url = "https://www.linkedin.com/jobs/search/?currentJobId=3349997861&f_AL=true&f_E=2&f_WT=2&keywords=python" \
      "%20developer%20&refresh=true&sortBy=R "


driver = webdriver.Remote(service.service_url)
driver.get(url)
time.sleep(3)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()

username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(email)

password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)

time.sleep(30)
driver.quit()
