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

novice_dataframe : pd.DataFrame = pd.concat([refinement_novice, inscription_novice, sigil_novice, nourishment_novice], ignore_index=True) # merging all Novice dataframes into one

# Initiate recipes
refinement_initiate = pd.read_html(url1, header=0)[0] # adding a dataframe for the refinement recipes
inscription_initiate : pd.DataFrame = pd.read_html(url1, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_initiate : pd.DataFrame = pd.read_html(url1, header=0)[4] # adding a dataframe for the Sigil recipes
nourishment_initiate : pd.DataFrame = pd.read_html(url1, header=0)[5] # adding a dataframe for the Nourishment recipes

initiate_dataframe : pd.DataFrame = pd.concat([refinement_initiate, inscription_initiate, sigil_initiate, nourishment_initiate], ignore_index=True) # merging all Initiate dataframes into one

# Apprentice recipes
refinement_apprentice = pd.read_html(url2, header=0)[0] # adding a dataframe for the refinement recipes
inscription_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[2] # adding a dataframe for the Inscription recipes
sigil_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[5] # adding a dataframe for the Sigil recipes
nourishment_apprentice : pd.DataFrame = pd.read_html(url2, header=0)[6] # adding a dataframe for the Nourishment recipes

apprentice_dataframe : pd.DataFrame = pd.concat([refinement_apprentice, inscription_apprentice, sigil_apprentice, nourishment_apprentice], ignore_index=True) # merging all Apprentice dataframes into one

# print(refinement_apprentice)
# print(inscription_apprentice)
# print(sigil_apprentice)
# print(nourishment_apprentice)

# data cleaning
novice_dataframe['Item'] = novice_dataframe['Item'].fillna(novice_dataframe['Name']) # replacing null values in the item column with the value in the name column
novice_dataframe.drop(columns=['Name'], inplace=True) # dropping the name column
novice_dataframe.drop(columns=['Discipline'], inplace=True) # dropping the Discipline column
novice_dataframe.drop(columns=['Trading Post'], inplace=True) # dropping the Trading Post column
novice_dataframe['Attributes'] = novice_dataframe['Attributes'].fillna('N.A.') # replacing the null values in Attributes with N.A.
novice_dataframe.drop(columns=['Discipline(s)'], inplace=True) # dropping the Output column
novice_dataframe['Crafting Level'] = novice_dataframe['Crafting Level'].fillna(novice_dataframe['Rating']) # replacing null values in the Crafting Level column with the value in the name Rating
novice_dataframe.drop(columns=['Rating'], inplace=True) # dropping the Rating column

with sqlite3.connect('gw2.db') as conn:
    novice_dataframe.to_sql('huntsman_crafting', conn, if_exists='replace', index=False)
    conn.commit()