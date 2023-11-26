import sqlite3
import pandas as pd

# getting the data from the wikipedia page

url = "https://wiki.guildwars2.com/wiki/Dungeon"

df = pd.read_html(url, header=0)[2]

# dropping the waypoint column
df.drop(['Waypoint'], axis=1, inplace=True)

# adding another table for the holiday dungeons

df2 = pd.read_html(url, header=0)[3]

# merging the two tables together
df = pd.concat([df, df2], axis=0)

# dropping the Suitable utility items column
df.drop(['Suitable utility items'], axis=1, inplace=True)

# data cleanup
df['Story Level'].fillna(80, inplace=True)
df['Explorable Level'].fillna('None', inplace=True)
df['Foe types [1]'].fillna('Multiple', inplace=True)
df['Day or Night 2'].fillna('N/A', inplace=True)
df['Initial Event / Duration'].fillna('N/A', inplace=True)
df['Availability'].fillna('Always', inplace=True)

with sqlite3.connect('gw2.db') as conn:
     df.to_sql('dungeons', conn, if_exists='replace', index=False)
     conn.commit()