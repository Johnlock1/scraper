from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

# request URL as an agent and save the HTML into webpage
req = Request('https://www.car.gr/classifieds/cars/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

# save the HTML inside every classified's div in one page
classifieds = soup.find_all("div", class_="clsfd_list_row_group")

# store all ids into list
# prefix = "http://www.car.gr/"
ids = []
for index, classified in enumerate(classifieds):
    ids.append(classifieds[index].a["href"].replace('/','').split('-')[0])

# store all cars' brand and model into list
brands = soup.find_all("span", class_="p_t")

cars = []
for index, brand in enumerate(brands):
    car = []
    car.append(brands[index].find(itemprop="brand").string)
    car.append(brands[index].find(itemprop="model").string)
    cars.append(car)

# merge ids list into cars list
for index, car in enumerate(ids):
    cars[index].append(ids[index])

for car in cars:
    print(car)