from datetime import datetime
from scraper import scrape
from export import export
from emails import send_email

today = datetime.today().strftime('%Y-%m-%d').text

url = "https://www.car.gr/classifieds/cars/?offer_type=sale&rg=2&significant_damage=t&st=private"
# url = "https://www.car.gr/classifieds/cars/?make=18" # for testing purposes

scrape(url)
export('cars', today)
send_email(today, 'email@email.com')