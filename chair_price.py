__author__ = 'john'

import requests
from bs4 import BeautifulSoup

content = requests.get("https://www.johnlewis.com/browse/home-garden/plants-planting/pots-planters/_/N-5urc").content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "product-card__price-span", "data-test":
                             "product-card__price product-card__price--current"})


string_price = element.text.strip()

price_without_symbol = string_price[1:]

price_float = float(price_without_symbol)

if price_float <30:
    print("Buy the chair already")
else:
    print("Too expensive")
