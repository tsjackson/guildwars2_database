import sqlite3
import pandas as pd
import os

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

url = "https://wiki.guildwars2.com/wiki/Leatherworker/Novice_recipes"
url2 = "https://wiki.guildwars2.com/wiki/Leatherworker/Apprentice_recipes"
url3 = "https://wiki.guildwars2.com/wiki/Leatherworker/Journeyman_recipes"
url4 = "https://wiki.guildwars2.com/wiki/Leatherworker/Adept_recipes"
url5 = "https://wiki.guildwars2.com/wiki/Leatherworker/Master_recipes"
url6 = "https://wiki.guildwars2.com/wiki/Leatherworker/Grandmaster_recipes"

# Novice recipes
insignia_novice = pd.read_html(url, header=0)[2] # adding a dataframe for the insignia recipes
rune_novice = pd.read_html(url, header=0)[5] # adding another dataframe for the rune recipes
refinement_novice = pd.read_html(url, header=0)[0] # adding another dataframe for the refinement recipes

# Apprentice recipes
insignia_apprentice = pd.read_html(url2, header=0)[2] # adding a dataframe for the insignia recipes
rune_apprentice = pd.read_html(url2, header=0)[2] # adding another dataframe for the rune recipes
refinement_apprentice = pd.read_html(url2, header=0)[0] # adding another dataframe for the refinement recipes

print(insignia_apprentice)
print(rune_apprentice)
print(refinement_apprentice)

# merging the dataframes together
leather_working = pd.concat([insignia_novice, rune_novice, refinement_novice, insignia_apprentice, rune_apprentice, refinement_apprentice], ignore_index=True)

# changing Rating column name
leather_working.rename(columns={'Rating': 'Level'}, inplace=True)

# dropping disciplines column
leather_working.drop(['Discipline(s)'], axis=1, inplace=True)

with sqlite3.connect('gw2.db') as conn:
    leather_working.to_sql('leather_crafting', conn, if_exists='replace', index=False)
    conn.commit()