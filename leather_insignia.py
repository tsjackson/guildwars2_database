import sqlite3
import pandas as pd

url = "https://wiki.guildwars2.com/wiki/Leatherworker/Novice_recipes"

df = pd.read_html(url, header=0)[2]

with sqlite3.connect('gw2.db') as conn:
    df.to_sql('leather_insignia', conn, if_exists='replace', index=False)
    conn.commit()