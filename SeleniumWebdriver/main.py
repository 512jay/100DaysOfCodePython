from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('/Development/chromedriver')

service.start()

driver = webdriver.Remote(service.service_url)
url = "https://www.python.org"
driver.get(url)

# title = driver.title
# print(title)
# driver.implicitly_wait(0.5)
#
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar)
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
#
# community_awards = driver.find_element(By.XPATH, value='//*[@id="container"]/li[4]/ul/li[11]/a')
# print(community_awards.text)

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")
# for event in events:
#     print(event.text)
# print(type(events))
# print(*events, sep="\n")
# print(events[0].text)
# item0 = events[0].text
# print(item0.split("\n"))
#  events_dictionary = {new_key: new_value for (key, value) in events if test}


def convert(lst):
    res_dct = {i: convert_item(lst[i]) for i in range(0, len(lst))}
    return res_dct


def convert_item(item):
    entry = item.text.split("\n")
    res_dct = {
        "time": entry[0],
        "name": entry[1]}
    return res_dct


event_dictionary = convert(events)
print(event_dictionary)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events_dict = {i: {"time": event_times[i].text, "name": event_names[i].text} for i in range(0, len(event_names))}
print(events_dict)
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[0].text,
        "name": event_names[0].text
    }
print(events)

driver.quit()
