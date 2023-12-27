import sqlite3
import pandas as pd
import os

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal, used for debugging purposes

url : str = "https://wiki.guildwars2.com/wiki/Tailor/Novice_recipes"
url1 : str = "https://wiki.guildwars2.com/wiki/Tailor/Initiate_recipes"
url2 : str = "https://wiki.guildwars2.com/wiki/Tailor/Apprentice_recipes"
url3 : str = "https://wiki.guildwars2.com/wiki/Tailor/Journeyman_recipes"
url4 : str = "https://wiki.guildwars2.com/wiki/Tailor/Adept_recipes"
url5 : str = "https://wiki.guildwars2.com/wiki/Tailor/Master_recipes"
url6 : str = "https://wiki.guildwars2.com/wiki/Tailor/Grandmaster_recipes"

# Novice recipes
print("Fetching Novice recipes")
insignia_novice = pd.read_html(url, header=0)[2] # adding a dataframe for the insignia recipes
rune_novice = pd.read_html(url, header=0)[5] # adding another dataframe for the rune recipes
refinement_novice = pd.read_html(url, header=0)[0] # adding another dataframe for the refinement recipes
bag_novice = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_novice = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

novice_dataframe = pd.concat([insignia_novice, rune_novice, refinement_novice,bag_novice,back_novice], ignore_index=True) # merging all Novice dataframes into one

# Initiate recipes
print("Fetching Initiate recipes")
insignia_initiate = pd.read_html(url1, header=0)[2] # adding a dataframe for the insignia recipes
rune_initiate = pd.read_html(url1, header=0)[5] # adding another dataframe for the rune recipes
refinement_initiate = pd.read_html(url1, header=0)[0] # adding another dataframe for the refinement recipes
bag_initiate = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_initiate = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

initiate_dataframe = pd.concat([insignia_initiate, rune_initiate, refinement_initiate,bag_initiate,back_initiate], ignore_index=True) # merging all Initiate dataframes into one

# Apprentice recipes
print("Fetching Apprentice recipes")
insignia_apprentice = pd.read_html(url2, header=0)[2] # adding a dataframe for the insignia recipes
rune_apprentice = pd.read_html(url2, header=0)[4] # adding another dataframe for the rune recipes
refinement_apprentice = pd.read_html(url2, header=0)[0] # adding another dataframe for the refinement recipes
bag_apprentice = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_apprentice = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

apprentice_dataframe = pd.concat([insignia_apprentice, rune_apprentice, refinement_apprentice, bag_apprentice,back_apprentice], ignore_index=True) # merging all Apprentice dataframes into one

# Journeyman recipes
print("Fetching Journeyman recipes")
insignia_journeyman = pd.read_html(url3, header=0)[2] # adding a dataframe for the insignia recipes
rune_journeyman = pd.read_html(url3, header=0)[5] # adding another dataframe for the rune recipes
refinement_journeyman = pd.read_html(url3, header=0)[0] # adding another dataframe for the refinement recipes
bag_journeyman = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_journeyman = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

journeyman_dataframe = pd.concat([insignia_journeyman, rune_journeyman, refinement_journeyman, bag_journeyman,back_journeyman], ignore_index=True) # merging all journeyman dataframes into one

# Adept recipes
print("Fetching Adept recipes")
insignia_adept = pd.read_html(url4, header=0)[2] # adding a dataframe for the insignia recipes
rune_adept = pd.read_html(url4, header=0)[4] # adding another dataframe for the rune recipes
refinement_adept = pd.read_html(url4, header=0)[0] # adding another dataframe for the refinement recipes
bag_adept = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_adept = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

adept_dataframe = pd.concat([insignia_adept, rune_adept, refinement_adept,bag_adept,back_adept], ignore_index=True) # merging all adept dataframes into one

# Master recipes
print("Fetching Master recipes")
insignia_master = pd.read_html(url5, header=0)[3] # adding a dataframe for the insignia recipes
rune_master = pd.read_html(url5, header=0)[5] # adding another dataframe for the rune recipes
refinement_master = pd.read_html(url5, header=0)[0] # adding another dataframe for the refinement recipes
bag_master = pd.read_html(url, header=0)[6] # adding another dataframe for the bag recipes
back_master = pd.read_html(url, header=0)[7] # adding another dataframe for the back recipes

master_dataframe = pd.concat([insignia_master, rune_master, refinement_master], ignore_index=True) # merging all master dataframes into one

# Grandmaster recipes
print("Fetching Grandmaster recipes")
insignia_grandmaster = pd.read_html(url6, header=0)[3] # adding a dataframe for the insignia recipes
# Grandmaster does not have runes
# Grandmaster does not have refinement

print("Merging all dataframes")
tailor_crafting = pd.concat([novice_dataframe, initiate_dataframe, apprentice_dataframe, journeyman_dataframe, adept_dataframe, master_dataframe, insignia_grandmaster], ignore_index=True) # merging all leatherworking dataframes into one

# print(insignia_grandmaster)
# print(rune_master)
# print(refinement_master)
# print(bag_master)
# print(back_master)

# data cleaning
print("Cleaning data")
tailor_crafting.rename(columns={'Rating': 'Level'}, inplace=True) # changing Rating column name
tailor_crafting.drop(['Discipline(s)'], axis=1, inplace=True) # dropping disciplines column
tailor_crafting = tailor_crafting[['Rarity', 'Level', 'Item', 'Ingredients']] # move the rarity column to the front
tailor_crafting.sort_values(by=['Level'], inplace=True) # sorting the dataframe by the level column

print('writing to database')
with sqlite3.connect('gw2.db') as conn:
    tailor_crafting.to_sql('tailor_crafting', conn, if_exists='replace', index=False)
    conn.commit()

print('Done')