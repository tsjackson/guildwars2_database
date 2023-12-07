import sqlite3
import pandas as pd
import os

os.system('cls' if os.name == 'nt' else 'clear') # clear the terminal, used for debugging purposes

url : str = "https://wiki.guildwars2.com/wiki/Huntsman/Novice_recipes"
url1 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Initiate_recipes"
url2 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Apprentice_recipes"
url3 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Journeyman_recipes"
url4 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Adept_recipes"
url5 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Master_recipes"
url6 : str = "https://wiki.guildwars2.com/wiki/Huntsman/Grandmaster_recipes"

# Novice recipes
print("Fetching Novice recipes")
refinement_novice : pd.DataFrame  = pd.read_html(url, header=0)[0] # adding a dataframe for the refinement recipes
inscription_novice : pd.DataFrame = pd.read_html(url, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_novice : pd.DataFrame = pd.read_html(url, header=0)[5] # adding a dataframe for the Sigil recipes
nourishment_novice : pd.DataFrame = pd.read_html(url, header=0)[6] # adding a dataframe for the Nourishment recipes

novice_dataframe : pd.DataFrame = pd.concat([refinement_novice, inscription_novice, sigil_novice, nourishment_novice], ignore_index=True) # merging all Novice dataframes into one

# Initiate recipes
print("Fetching Initiate recipes")
refinement_initiate = pd.read_html(url1, header=0)[0] # adding a dataframe for the refinement recipes
inscription_initiate : pd.DataFrame = pd.read_html(url1, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_initiate : pd.DataFrame = pd.read_html(url1, header=0)[4] # adding a dataframe for the Sigil recipes
nourishment_initiate : pd.DataFrame = pd.read_html(url1, header=0)[5] # adding a dataframe for the Nourishment recipes

initiate_dataframe : pd.DataFrame = pd.concat([refinement_initiate, inscription_initiate, sigil_initiate, nourishment_initiate], ignore_index=True) # merging all Initiate dataframes into one

# Apprentice recipes
print("Fetching Apprentice recipes")
refinement_apprentice = pd.read_html(url2, header=0)[0] # adding a dataframe for the refinement recipes
inscription_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[5] # adding a dataframe for the Sigil recipes
nourishment_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[6] # adding a dataframe for the Nourishment recipes

apprentice_dataframe : pd.DataFrame = pd.concat([refinement_apprentice, inscription_apprentice, sigil_apprentice, nourishment_apprentice], ignore_index=True) # merging all Apprentice dataframes into one

# Journeyman recipes
print("Fetching Journeyman recipes")
refinement_journeyman = pd.read_html(url3, header=0)[0] # adding a dataframe for the refinement recipes
inscription_journeyman : pd.DataFrame = pd.read_html(url3, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_journeyman : pd.DataFrame = pd.read_html(url3, header=0)[5] # adding a dataframe for the Sigil recipes
nourishment_journeyman : pd.DataFrame = pd.read_html(url3, header=0)[6] # adding a dataframe for the Nourishment recipes

journeyman_dataframe : pd.DataFrame = pd.concat([refinement_journeyman, inscription_journeyman, sigil_journeyman, nourishment_journeyman], ignore_index=True) # merging all Journeyman dataframes into one

# Adept recipes
print("Fetching Adept recipes")
refinement_adept = pd.read_html(url4, header=0)[0] # adding a dataframe for the refinement recipes
inscription_adept : pd.DataFrame = pd.read_html(url4, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_adept : pd.DataFrame = pd.read_html(url4, header=0)[4] # adding a dataframe for the Sigil recipes
nourishment_adept : pd.DataFrame = pd.read_html(url4, header=0)[5] # adding a dataframe for the Nourishment recipes

adept_dataframe : pd.DataFrame = pd.concat([refinement_adept, inscription_adept, sigil_adept, nourishment_adept], ignore_index=True) # merging all Adept dataframes into one

# Master recipes
print("Fetching Master recipes")
refinement_master = pd.read_html(url5, header=0)[0] # adding a dataframe for the refinement recipes
ectoplasm_master : pd.DataFrame = pd.read_html(url5, header=0)[1] # adding a dataframe for the Ectoplasm recipes
obsidian_master : pd.DataFrame = pd.read_html(url5, header=0)[2] # adding a dataframe for the Obsidian recipes
inscription_master : pd.DataFrame = pd.read_html(url5, header=0)[5] # adding a dataframe for the Inscription recipes
sigil_master : pd.DataFrame = pd.read_html(url5, header=0)[8] # adding a dataframe for the Sigil recipes
nourishment_master : pd.DataFrame = pd.read_html(url5, header=0)[9] # adding a dataframe for the Nourishment recipes

master_dataframe : pd.DataFrame = pd.concat([refinement_master, ectoplasm_master, inscription_master, obsidian_master, sigil_master, nourishment_master], ignore_index=True) # merging all Master dataframes into one

# Grandmaster recipes
print("Fetching Grandmaster recipes")
refinement_grandmaster = pd.read_html(url6, header=0)[0] # adding a dataframe for the refinement recipes
vision_crystal : pd.DataFrame = pd.read_html(url6, header=0)[2] # adding a dataframe for the Obsidian recipes
inscription_grandmaster : pd.DataFrame = pd.read_html(url6, header=0)[3] # adding a dataframe for the Inscription recipes
# Grandmaster does not have sigils
# grandmaster does not have nourishment

grandmaster_dataframe : pd.DataFrame = pd.concat([refinement_grandmaster, inscription_grandmaster, vision_crystal], ignore_index=True) # merging all Grandmaster dataframes into one

# print(refinement_grandmaster)
# print(vision_crystal)
# print(inscription_grandmaster)
# print(inscription_master)
# print(sigil_master)
# print(nourishment_master)

print("Merging all huntsman dataframes into one")
huntsman_dataframe : pd.DataFrame = pd.concat([novice_dataframe, initiate_dataframe, apprentice_dataframe, journeyman_dataframe, adept_dataframe, master_dataframe, grandmaster_dataframe], ignore_index=True) # merging all huntsman dataframes into one

# data cleaning
print("Cleaning data")
huntsman_dataframe['Item'] = huntsman_dataframe['Item'].fillna(huntsman_dataframe['Name']) # replacing null values in the item column with the value in the name column
huntsman_dataframe.drop(columns=['Name'], inplace=True) # dropping the name column
huntsman_dataframe.drop(columns=['Discipline'], inplace=True) # dropping the Discipline column
huntsman_dataframe.drop(columns=['Trading Post'], inplace=True) # dropping the Trading Post column
huntsman_dataframe['Attributes'] = huntsman_dataframe['Attributes'].fillna('N.A.') # replacing the null values in Attributes with N.A.
huntsman_dataframe.drop(columns=['Discipline(s)'], inplace=True) # dropping the Output column
huntsman_dataframe['Crafting Level'] = huntsman_dataframe['Crafting Level'].fillna(huntsman_dataframe['Rating']) # replacing null values in the Crafting Level column with the value in the name Rating
huntsman_dataframe.drop(columns=['Rating'], inplace=True) # dropping the Rating column

print('Writing to the database')
with sqlite3.connect('gw2.db') as conn:
    huntsman_dataframe.to_sql('huntsman_crafting', conn, if_exists='replace', index=False)
    conn.commit()

print('Done')