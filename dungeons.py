import sqlite3
import pandas as pd
import numpy as np

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Dungeon"

df = pd.read_html(url, header=0)[2]

# dropping the waypoint column
df.drop(['Waypoint'], axis=1, inplace=True)

# replacing the NULL values with N/A
df.fillna('N/A', inplace=True)

# adding another table for the holiday dungeons

df2 = pd.read_html(url, header=0)[3]

print(df2)

with sqlite3.connect('gw2.db') as conn:
     df.to_sql('dungeons', conn, if_exists='replace', index=False)
     conn.commit()

with sqlite3.connect('gw2.db') as conn:
     df2.to_sql('holiday_dungeons', conn, if_exists='replace', index=False)
     conn.commit()