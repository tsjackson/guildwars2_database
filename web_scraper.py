# creating a web scraper to scrape the data from the wikipedia page and then store it in a csv file

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from pprint import pprint

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Rune"

# getting the data from the url
data = requests.get(url)

# converting the data to a beautifulsoup object
soup = BeautifulSoup(data.text, 'html.parser')

# getting the table from the soup object
table = soup.find('table', {'class': 'item table'})

# getting the table rows from the table
table_rows = table.find_all('tr')

# creating a list to store the data
data = []

# looping through the table rows and getting the data
for row in table_rows:
    data.append([t.text.strip() for t in row.find_all('td')])

pprint(data)

# creating a dataframe from the data
# df = pd.DataFrame(data, columns=['Rune', 'Type', 'Major 1', 'Major 2', 'Major 3', 'Major 4', 'Major 5', 'Minor 1', 'Minor 2', 'Minor 3', 'Minor 4', 'Minor 5'])