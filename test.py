from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

# Request URL as an agent and save the HTML into wepage
req = Request('https://www.car.gr/classifieds/cars/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

print(soup.prettify())