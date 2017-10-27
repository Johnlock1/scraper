from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

# request URL as an agent and save the HTML into wepage
req = Request('https://www.car.gr/classifieds/cars/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

# save the HTML inside every classified's div in one page
classifieds = soup.find_all("div", class_="clsfd_list_row_group")

# store all links into list
prefix = "http://www.car.gr"
links = []
for classified in classifieds:
    links.append(prefix + classifieds[0].a["href"])

print(links)