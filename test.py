from cs50 import SQL
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen

def scrape(url):
    db = SQL("sqlite:///database.db")
    database = []

    # request URL as an agent and save the HTML into webpage
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")

    # get number of total pages
    page = soup.find("ul", "pagination pull-right")
    li = page.find_all("li", class_="")
    pages = li[1].a["href"].split('pg=')[1]
    if '&' in pages:
        pages = int(pages.split('&')[0])
    print(pages)

    # scrape multiple pages
    for i in range(pages):
        print('Page {}'.format(url+'&pg={}').format(i+1))
        # request URL as an agent and save the HTML into webpage
        req = Request('{}'.format(url+'&pg={}').format(i+1),
                        headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, "html.parser")

        # store all ids into list
        classifieds = soup.find_all("div", class_="clsfd_list_row_group")

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
            year = brands[index].find(itemprop="releaseDate").string.replace("`","")
            if int(year) >= 00 and int(year) < 20:
                year = "20" + year
            else:
                year = "19" + year
            car.append(int(year))
            cars.append(car)

        # store all car's price
        values = soup.find_all("h2", class_="text-right")

        prices = []
        for index, value in enumerate(values):
            price = values[index].find(itemprop="price").string
            if price == "Ρωτήστε τιμή":
                prices.append(0)
            else:
                prices.append(int(price.replace('.', '').replace('€\xa0', '')))

        # merge ids and prices list into cars list
        for index, car in enumerate(cars):
            item = ids[index]
            car.insert(0, item)
            car.append(prices[index])

        print("Page {}".format(i+1))
        for car in cars:
            print(car)
        print("\n")

        for car in cars:
            database.append(car)

    print("End with pages")

    # iterate through every car in cars
    for index, row in enumerate(database):
        car_id = database[index][0]
        req = Request('https://www.car.gr/{}'.format(car_id), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, "html.parser")

        # append phone into cars
        database[index].append(soup.find("h3", class_="details-header").string.split("Τηλέφωνο: ")[1].split(" ")[0])

    print("Starting database insertion")
    for index, row in enumerate(database):
        print(index)

        # check if id is in database
        result = db.execute("SELECT car_id FROM cars WHERE car_id = :car_id", car_id = database[index][0])
        if result != 1:
            print("Inserting...")
            db.execute("INSERT INTO cars (car_id, make, model, year, price, phone) \
                    VALUES (:car_id, :make, :model, :year, :price, :phone)",
                    car_id=database[index][0],
                    make=database[index][1],
                    model=database[index][2],
                    year=database[index][3],
                    price=database[index][4],
                    phone=database[index][5])

    print("Success")