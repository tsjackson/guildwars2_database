import sqlite3
import pandas as pd
import os

# clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

url = "https://wiki.guildwars2.com/wiki/Leatherworker/Novice_recipes"
url1 = "https://wiki.guildwars2.com/wiki/Leatherworker/Initiate_recipes"
url2 = "https://wiki.guildwars2.com/wiki/Leatherworker/Apprentice_recipes"
url3 = "https://wiki.guildwars2.com/wiki/Leatherworker/Journeyman_recipes"
url4 = "https://wiki.guildwars2.com/wiki/Leatherworker/Adept_recipes"
url5 = "https://wiki.guildwars2.com/wiki/Leatherworker/Master_recipes"
url6 = "https://wiki.guildwars2.com/wiki/Leatherworker/Grandmaster_recipes"

# Novice recipes
insignia_novice = pd.read_html(url, header=0)[2] # adding a dataframe for the insignia recipes
rune_novice = pd.read_html(url, header=0)[5] # adding another dataframe for the rune recipes
refinement_novice = pd.read_html(url, header=0)[0] # adding another dataframe for the refinement recipes

novice_dataframe = pd.concat([insignia_novice, rune_novice, refinement_novice], ignore_index=True) # merging all Novice dataframes into one

# Initiate recipes
insignia_initiate = pd.read_html(url1, header=0)[2] # adding a dataframe for the insignia recipes
rune_initiate = pd.read_html(url1, header=0)[4] # adding another dataframe for the rune recipes
refinement_initiate = pd.read_html(url1, header=0)[0] # adding another dataframe for the refinement recipes

initiate_dataframe = pd.concat([insignia_initiate, rune_initiate, refinement_initiate], ignore_index=True) # merging all Initiate dataframes into one

# Apprentice recipes
insignia_apprentice = pd.read_html(url2, header=0)[2] # adding a dataframe for the insignia recipes
rune_apprentice = pd.read_html(url2, header=0)[4] # adding another dataframe for the rune recipes
refinement_apprentice = pd.read_html(url2, header=0)[0] # adding another dataframe for the refinement recipes

apprentice_dataframe = pd.concat([insignia_apprentice, rune_apprentice, refinement_apprentice], ignore_index=True) # merging all Apprentice dataframes into one

# Journeyman recipes
insignia_journeyman = pd.read_html(url3, header=0)[2] # adding a dataframe for the insignia recipes
rune_journeyman = pd.read_html(url3, header=0)[5] # adding another dataframe for the rune recipes
refinement_journeyman = pd.read_html(url3, header=0)[0] # adding another dataframe for the refinement recipes

journeyman_dataframe = pd.concat([insignia_journeyman, rune_journeyman, refinement_journeyman], ignore_index=True) # merging all journeyman dataframes into one

# Adept recipes
insignia_adept = pd.read_html(url4, header=0)[2] # adding a dataframe for the insignia recipes
rune_adept = pd.read_html(url4, header=0)[4] # adding another dataframe for the rune recipes
refinement_adept = pd.read_html(url4, header=0)[0] # adding another dataframe for the refinement recipes

adept_dataframe = pd.concat([insignia_adept, rune_adept, refinement_adept], ignore_index=True) # merging all adept dataframes into one

# Master recipes
insignia_master = pd.read_html(url5, header=0)[3] # adding a dataframe for the insignia recipes
rune_master = pd.read_html(url5, header=0)[5] # adding another dataframe for the rune recipes
refinement_master = pd.read_html(url5, header=0)[0] # adding another dataframe for the refinement recipes

master_dataframe = pd.concat([insignia_master, rune_master, refinement_master], ignore_index=True) # merging all master dataframes into one

# Grandmaster recipes
insignia_grandmaster = pd.read_html(url6, header=0)[3] # adding a dataframe for the insignia recipes
# Grandmaster does not have runes
# Grandmaster does not have refinement

leather_working = pd.concat([novice_dataframe, initiate_dataframe, apprentice_dataframe, journeyman_dataframe, adept_dataframe, master_dataframe, insignia_grandmaster], ignore_index=True) # merging all leatherworking dataframes into one

# data cleaning
leather_working.rename(columns={'Rating': 'Level'}, inplace=True) # changing Rating column name
leather_working.drop(['Discipline(s)'], axis=1, inplace=True) # dropping disciplines column

with sqlite3.connect('gw2.db') as conn:
    leather_working.to_sql('leather_crafting', conn, if_exists='replace', index=False)
    conn.commit()