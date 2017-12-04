from export import export
from test import scrape
import datetime

day = datetime.datetime.now().strftime('%Y-%m-%d')
day = "{}".format(day)

scrape()
export('cars', day)