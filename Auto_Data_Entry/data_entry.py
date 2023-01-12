import requests
from bs4 import BeautifulSoup
# import os


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                  "Safari/537.36",
}

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeSje4g5_LwswlvWkjAAYopsu7ZJo6dRzpjakbQFn8wiqpQ3A/viewform?usp" \
           "=sf_link"

zillow_url = "https://www.zillow.com/washington-dc/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22north%22%3A39.09992434478873%2C%22east%22%3A-76.75399402978515%2C%22south%22" \
             "%3A38.68681428804895%2C%22west%22%3A-77.27515797021483%7D%2C%22mapZoom%22%3A11%2C%22regionSelection%22" \
             "%3A%5B%7B%22regionId%22%3A41568%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C" \
             "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A419992%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C" \
             "%22baths%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22" \
             "%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A" \
             "%7B%22value%22%3Atrue%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse" \
             "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C" \
             "%22isListVisible%22%3Atrue%7D"

response = requests.get(zillow_url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
# new_list = [new_item for item in list if test]
addresses = [address.text for address in soup.find_all('address')]
listings = [listing for listing in soup.find_all(class_='property-card-data')]
count = 1
for listing in listings:
    print(f"{count}:: {listing.text}")
    count += 1
print("\n******\n")
links = [link for link in soup.find_all('a', class_='property-card-link')]
count = 1
for link in links:
    print(f"{count}:: {link}")
    count += 1


# TODO Create a list of links for all the listings you scraped

# TODO Create a list of prices for all the listings you scraped

# TODO Create a list of addresses for all the listings you scraped.

# TODO Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its
#  price/address/link added to the form. You will need to fill in a new form for each new listing.

# TODO Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to
#  the Google Form. You should end up with a spreadsheet with all the details from the properties.
