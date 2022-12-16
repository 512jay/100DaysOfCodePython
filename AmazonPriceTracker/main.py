import requests
from bs4 import BeautifulSoup
import smtplib
import os

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
GMAIL = os.environ.get("GMAIL")
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")
YAHOO = os.environ.get("YAHOO")


def send_email(email_address, email_subject, email_message):
    msg = f"Subject:{email_subject}\n\n{email_message}"
    with smtplib.SMTP(GMAIL_SMTP) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=email_address,
            msg=msg
        )


target_price = 150
if price < target_price:
    subject = "Amazon Low Price Alert!"
    message = f"{soup.title.text}\nnow ${price}\n{url}"
    send_email(email_address=YAHOO, email_subject=subject, email_message=message)
else:
    print("The price is still too damn high!")
