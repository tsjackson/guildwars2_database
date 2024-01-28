import sqlite3
import pandas as pd
import os

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal, used for debugging purposes

novice_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Novice_recipes"
initiate_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Initiate_recipes"
apprentice_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Apprentice_recipes"
journeyman_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Journeyman_recipes"
adept_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Adept_recipes"
master_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Master_recipes"
grandmaster_url : str = "https://wiki.guildwars2.com/wiki/Armorsmith/Grandmaster_recipes"

# Novice recipes
print("Fetching Novice recipes")
whole_novice = pd.read_html(novice_url, header=0) # adding a dataframe for the insignia recipes
insignia_novice = pd.read_html(novice_url, header=0)[2] # adding a dataframe for the insignia recipes
rune_novice = pd.read_html(novice_url, header=0)[5] # adding another dataframe for the rune recipes
refinement_novice = pd.read_html(novice_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_novice = pd.read_html(novice_url, header=0)[6] # adding another dataframe for the bag recipes
back_novice = pd.read_html(novice_url, header=0)[7] # adding another dataframe for the back recipes

novice_dataframe = pd.concat([insignia_novice, rune_novice, refinement_novice,bag_novice,back_novice], ignore_index=True) # merging all Novice dataframes into one

# Initiate recipes
print("Fetching Initiate recipes")
insignia_initiate = pd.read_html(initiate_url, header=0)[2] # adding a dataframe for the insignia recipes
rune_initiate = pd.read_html(initiate_url, header=0)[4] # adding another dataframe for the rune recipes
refinement_initiate = pd.read_html(initiate_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_initiate = pd.read_html(initiate_url, header=0)[5] # adding another dataframe for the bag recipes
back_initiate = pd.read_html(initiate_url, header=0)[6] # adding another dataframe for the back recipes

initiate_dataframe = pd.concat([insignia_initiate, rune_initiate, refinement_initiate,bag_initiate,back_initiate], ignore_index=True) # merging all Initiate dataframes into one

# Apprentice recipes
print("Fetching Apprentice recipes")
insignia_apprentice = pd.read_html(apprentice_url, header=0)[2] # adding a dataframe for the insignia recipes
rune_apprentice = pd.read_html(apprentice_url, header=0)[4] # adding another dataframe for the rune recipes
refinement_apprentice = pd.read_html(apprentice_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_apprentice = pd.read_html(apprentice_url, header=0)[5] # adding another dataframe for the bag recipes
back_apprentice = pd.read_html(apprentice_url, header=0)[6] # adding another dataframe for the back recipes

apprentice_dataframe = pd.concat([insignia_apprentice, rune_apprentice, refinement_apprentice, bag_apprentice,back_apprentice], ignore_index=True) # merging all Apprentice dataframes into one

# Journeyman recipes
print("Fetching Journeyman recipes")
insignia_journeyman = pd.read_html(journeyman_url, header=0)[2] # adding a dataframe for the insignia recipes
rune_journeyman = pd.read_html(journeyman_url, header=0)[5] # adding another dataframe for the rune recipes
refinement_journeyman = pd.read_html(journeyman_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_journeyman = pd.read_html(journeyman_url, header=0)[6] # adding another dataframe for the bag recipes
back_journeyman = pd.read_html(journeyman_url, header=0)[7] # adding another dataframe for the back recipes

journeyman_dataframe = pd.concat([insignia_journeyman, rune_journeyman, refinement_journeyman, bag_journeyman,back_journeyman], ignore_index=True) # merging all journeyman dataframes into one

# Adept recipes
print("Fetching Adept recipes")
insignia_adept = pd.read_html(adept_url, header=0)[2] # adding a dataframe for the insignia recipes
rune_adept = pd.read_html(adept_url, header=0)[4] # adding another dataframe for the rune recipes
refinement_adept = pd.read_html(adept_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_adept = pd.read_html(adept_url, header=0)[5] # adding another dataframe for the bag recipes
back_adept = pd.read_html(adept_url, header=0)[6] # adding another dataframe for the back recipes

adept_dataframe = pd.concat([insignia_adept, rune_adept, refinement_adept,bag_adept,back_adept], ignore_index=True) # merging all adept dataframes into one

# Master recipes
print("Fetching Master recipes")
insignia_master = pd.read_html(master_url, header=0)[3] # adding a dataframe for the insignia recipes
rune_master = pd.read_html(master_url, header=0)[5] # adding another dataframe for the rune recipes
refinement_master = pd.read_html(master_url, header=0)[0] # adding another dataframe for the refinement recipes
bag_master = pd.read_html(master_url, header=0)[6] # adding another dataframe for the bag recipes
back_master = pd.read_html(master_url, header=0)[7] # adding another dataframe for the back recipes

master_dataframe = pd.concat([insignia_master, rune_master, refinement_master], ignore_index=True) # merging all master dataframes into one

# Grandmaster recipes
print("Fetching Grandmaster recipes")
insignia_grandmaster = pd.read_html(grandmaster_url, header=0)[3] # adding a dataframe for the insignia recipes
# Grandmaster does not have runes
# Grandmaster does not have refinement
bag_grandmaster = pd.read_html(grandmaster_url, header=0)[4] # adding another dataframe for the bag recipes

grandmaster_dataframe = pd.concat([insignia_grandmaster, bag_grandmaster], ignore_index=True) # merging all grandmaster dataframes into one

# print("Merging all dataframes")
armorsmith_dataframe = pd.concat([novice_dataframe, initiate_dataframe, apprentice_dataframe, journeyman_dataframe, adept_dataframe, master_dataframe, grandmaster_dataframe], ignore_index=True) # merging all dataframes into one

# data cleaning
print("Cleaning data")
armorsmith_dataframe.rename(columns={'Rating': 'Level'}, inplace=True) # changing Rating column name
armorsmith_dataframe.drop(['Discipline(s)'], axis=1, inplace=True) # dropping disciplines column
armorsmith_dataframe = armorsmith_dataframe[['Rarity', 'Level', 'Item', 'Ingredients']] # move the rarity column to the front
armorsmith_dataframe.sort_values(by=['Level'], inplace=True) # sorting the dataframe by the level column

print('writing to database')
with sqlite3.connect('gw2.db') as conn:
    armorsmith_dataframe.to_sql('armorsmith_crafting', conn, if_exists='replace', index=False)
    conn.commit()

print('Done')