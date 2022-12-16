import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36 "
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price_soup = soup.find(class_="a-price-whole")
price = float(price_soup.text)

#  Begin part 2
target_price = 180
if price < target_price:
    subject = "Amazon Price Alert!"
    message = f"{soup.title.text}\nnow ${price}\n{url}"
    print(subject, "\n", message)
