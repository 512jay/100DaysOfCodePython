from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/Development/chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)
url = "https://orteil.dashnet.org/cookieclicker/"

driver.get(url)
time.sleep(5)
english = driver.find_element(by=By.ID, value="langSelect-EN")
english.click()
time.sleep(5)
annoy = driver.find_element(by=By.LINK_TEXT, value="Got it!")
annoy.click()
timeout = 60 * 5
check_products = 20
timeout_start = time.time()
cookie = driver.find_element(by=By.ID, value="bigCookie")


def product_check():
    products = driver.find_elements(by=By.CLASS_NAME, value="product.unlocked.enabled")
    if len(products) > 0:
        products[-1].click()


while time.time() < timeout_start + timeout:
    cookie.click()
    product_check()

cookies_per_second = driver.find_element(by=By.ID, value="cookies")
print(cookies_per_second.text)
