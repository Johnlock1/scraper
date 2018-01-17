import datetime
from scraper import scrape
from export import export
from email import send_email

day = datetime.datetime.now().strftime('%Y-%m-%d')
day = "{}".format(day)

url = "https://www.car.gr/classifieds/cars/?offer_type=sale&rg=2&significant_damage=t&st=private"
# url = "https://www.car.gr/classifieds/cars/?make=18" # for testing purposes

scrape(url)
export('cars', day)
send_email(day, 'email@email.com')