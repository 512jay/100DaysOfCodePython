# from bs4 import BeautifulSoup


form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeSje4g5_LwswlvWkjAAYopsu7ZJo6dRzpjakbQFn8wiqpQ3A/viewform?usp" \
           "=sf_link"

zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22" \
             "%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37" \
             ".696824250395%2C%22north%22%3A37.85367546337887%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C" \
             "%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C" \
             "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22" \
             "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22" \
             "%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22" \
             "%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

# TODO Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address

# TODO Create a list of links for all the listings you scraped

# TODO Create a list of prices for all the listings you scraped

# TODO Create a list of addresses for all the listings you scraped.

# TODO Use Selenium to fill in the form you created (step 1,2,3 above). Each listing should have its
#  price/address/link added to the form. You will need to fill in a new form for each new listing.

# TODO Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to
#  the Google Form. You should end up with a spreadsheet with all the details from the properties.
