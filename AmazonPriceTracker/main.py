import requests
from bs4 import BeautifulSoup

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36 "
}
url = "https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/"
response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.title)
