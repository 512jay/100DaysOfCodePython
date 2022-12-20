from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service('/Development/chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)
# url = "https://en.wikipedia.org/wiki/Main_Page"
# url = "https://www.appbrewery.co/p/newsletter"
url = "https://orteil.dashnet.org/cookieclicker/"
driver.get(url)
#
# signup = driver.find_element(By.ID, "email")
# signup.send_keys("developercroesus@gmail.com")
# signup.send_keys(Keys.ENTER)

# num_of_articles = driver.find_element(by=By.ID, value="articlecount")
# print(num_of_articles.text.split()[0])
#
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)
# article_count.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


time.sleep(5)
driver.quit()

