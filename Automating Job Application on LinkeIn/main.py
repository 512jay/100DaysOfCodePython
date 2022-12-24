from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/Development/chromedriver')

service.start()

url = "https://www.linkedin.com/jobs/search/?currentJobId=3349997861&f_AL=true&f_E=2&f_WT=2&keywords=python%20developer%20&refresh=true&sortBy=R"


driver = webdriver.Remote(service.service_url)
driver.get(url)
time.sleep(5)
sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in.click()
time.sleep(30)
driver.quit()
