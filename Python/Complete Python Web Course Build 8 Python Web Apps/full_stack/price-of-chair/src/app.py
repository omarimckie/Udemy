__author__ = 'omari'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.flightclub.com/air-jordan-12-retro-black-game-royal-154517?size=9")
content = request.content
# the BeautifulSoup that we imported can help us parse through the content that we have stored in the variable
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"class": "price"})
# print(element.text.strip()) if this has a number sign attached, you need to do some splicing

string_price = element.text.strip()
price_without_symbol = string_price[1:] # this is called splicing, it takes the string and instead of starting at 0, it will start at position 1

price = float(string_price)

# will print to buy the item if it is under $200, if not, print to hold off
if(price < 200):
    print("Buy the shoes now!")
    print("the current price is {}".format(price))
else:
    print("hold off for now")
    print("the current price is ${}0".format(price))
