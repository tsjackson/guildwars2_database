# creating a web scraper to scrape the data from the wikipedia page and then store it in a csv file

import pandas as pd
import numpy as np
from pprint import pprint

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Rune"

df = pd.read_html(url, header=0)[0]

# delete first row

df = df.iloc[1:]

df.to_csv("runes.csv", index=False)

pprint(df)