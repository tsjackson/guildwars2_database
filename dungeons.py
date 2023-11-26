import sqlite3
import pandas as pd
import numpy as np
from pprint import pprint

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Dungeon"

df = pd.read_html(url, header=0)[2]

# dropping the waypoint column
df.drop(['Waypoint'], axis=1, inplace=True)

pprint(df)

with sqlite3.connect('gw2.db') as conn:
    df.to_sql('dungeons', conn, if_exists='replace', index=False)
    conn.commit()