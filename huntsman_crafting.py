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
refinement_novice = pd.read_html(url, header=0)[0] # adding a dataframe for the refinement recipes
inscription_novice : pd.DataFrame = pd.read_html(url, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_novice : pd.DataFrame = pd.read_html(url, header=0)[5] # adding a dataframe for the Sigil recipes
nourishment_novice : pd.DataFrame = pd.read_html(url, header=0)[6] # adding a dataframe for the Nourishment recipes

novice_dataframe = pd.concat([refinement_novice, inscription_novice, sigil_novice, nourishment_novice], ignore_index=True) # merging all Novice dataframes into one

# data cleaning
novice_dataframe['Item'] = novice_dataframe['Item'].fillna(novice_dataframe['Name']) # replacing null values in the item column with the value in the name column
novice_dataframe.drop(columns=['Name'], inplace=True) # dropping the name column
novice_dataframe.drop(columns=['Discipline'], inplace=True) # dropping the Discipline column
novice_dataframe.drop(columns=['Trading Post'], inplace=True) # dropping the Trading Post column
novice_dataframe['Attributes'] = novice_dataframe['Attributes'].fillna('N.A.') # replacing the null values in Attributes with N.A.
novice_dataframe.drop(columns=['Discipline(s)'], inplace=True) # dropping the Output column
novice_dataframe['Crafting Level'] = novice_dataframe['Crafting Level'].fillna(novice_dataframe['Rating']) # replacing null values in the Crafting Level column with the value in the name Rating
novice_dataframe.drop(columns=['Rating'], inplace=True) # dropping the Rating column


# print(refinement_novice)
# print(inscription_novice)
# print(sigil_novice)
# print(nourishment_novice)

with sqlite3.connect('gw2.db') as conn:
    novice_dataframe.to_sql('huntsman_crafting', conn, if_exists='replace', index=False)
    conn.commit()