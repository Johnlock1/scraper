from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

# request URL as an agent and save the HTML into webpage
req = Request('https://www.car.gr/classifieds/cars/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, "html.parser")

# save the HTML inside every classified's div in one page
classifieds = soup.find_all("div", class_="clsfd_list_row_group")

# store all links into list
prefix = "http://www.car.gr"
links = []
for index, classified in enumerate(classifieds):
    links.append(prefix + classifieds[index].a["href"])
#print(links)

# store all cars' brand and model into list
brands = soup.find_all("span", class_="p_t")

cars = []
for index, brand in enumerate(brands):
    car = []
    car.append(brands[index].find(itemprop="brand").string)
    car.append(brands[index].find(itemprop="model").string)
    cars.append(car)

# merge links list into cars list
for index, car in enumerate(links):
    cars[index].append(links[index])
    
print(cars)

