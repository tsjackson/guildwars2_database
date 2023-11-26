# creating a web scraper to scrape the data from the wikipedia page and then store it in a database

import sqlite3
import pandas as pd
import numpy as np

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Rune"

df = pd.read_html(url, header=0)[0]

# creating a column for the type of rune
df['Quality'] = np.where(df['Rune'].str.contains('Superior'), 'Superior', 'Major')

# creating columns for the bonuses
df['Type'] = df['Bonus 1'].str.split(' ', expand=True)[1]

df['Type'] = np.where(df['Type'].str.contains('to'), 'All', df['Type'])

# if quality is major, delete record
df.drop(df[df['Quality'] == 'Major'].index, inplace=True)

# Moving Quality and type columns to the front
cols = df.columns.tolist()
cols = cols[-2:] + cols[:-2]
df = df[cols]

with sqlite3.connect('gw2.db') as conn:
    df.to_sql('runes', conn, if_exists='replace', index=False)
    conn.commit()