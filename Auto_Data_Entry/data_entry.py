import requests
from bs4 import BeautifulSoup
from inputs import zillow_url, headers
import time

response = requests.get(zillow_url, headers=headers)
time.sleep(2)
soup = BeautifulSoup(response.text, 'html.parser')
# new_list = [new_item for item in list if test]
result_count = soup.find(class_="result-count")
print(result_count.text)


def get_prices() -> list:
    prices = []
    spans = soup.find_all("span")
    for span in spans:
        try:
            if span['data-test'] == 'property-card-price':
                prices.append(span.text[0:6])
        except KeyError:
            pass
    return prices


def get_addresses():
    addresses_list = [address.text for address in soup.find_all('address')]
    addresses = []
    for address in addresses_list:
        try:
            addresses.append(address.split('|')[1])
        except IndexError:
            addresses.append(address)
    return addresses


def get_links():
    links = [link for link in soup.find_all('a', class_='property-card-link')]
    return links


print(get_addresses())
print(get_prices())
print(get_links())

# for listing in listings:
#     print(f"{count}:: {listing.text}")
#     count += 1
# print("\n******\n")
# count = 1
# for link in links:
#     print(f"{count}:: {link}")
#     count += 1
# TODO Create a list of links for all the listings you scraped

# TODO Create a list of prices for all the listings you scraped

# TODO Create a list of addresses for all the listings you scraped.

# TODO Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its
#  price/address/link added to the form. You will need to fill in a new form for each new listing.

# TODO Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to
#  the Google Form. You should end up with a spreadsheet with all the details from the properties.
