import streamlit as st
import pandas as pd
import sqlite3 as sql

# to start streamlit, run the following command in the terminal
# streamlit run dashboard.py

# to stop streamlit, press ctrl + c in the terminal

# to run streamlit in the background, run the following command in the terminal
# streamlit run dashboard.py &
# to stop streamlit, run the following command in the terminal
# fg
# ctrl + c
# creating a connection to the database and getting the data
with sql.connect('gw2.db') as conn:
    st.title('Guild Wars 2 Database')

    database_selection = st.radio('Select Database', ['dungeons','leather_crafting','runes'])

    df = pd.read_sql(f'SELECT * FROM {database_selection}', conn)

    with st.expander('Fuck Frost, I have a database!'):
        if database_selection == 'runes':

            # creating a sidebar to select the rune type
                st.sidebar.header('Select Rune Type')

                type_search = st.sidebar.multiselect('Search by Rune Type',df['Type'].unique())

                if type_search == []:
                    type_search = df['Type'].unique()

                filter = df['Type'].isin(type_search)
                df = df[filter]

                name_search = st.sidebar.multiselect('Search by Rune Name',df['Rune'].unique())

                if name_search == []:
                    name_search = df['Rune'].unique()

                filter = df['Rune'].isin(name_search)
                df = df[filter]

                st.table(df)
        elif database_selection == 'dungeons':
                # creating a sidebar to select the dungeon
                st.sidebar.header('Select Dungeon')

                dungeon_search = st.sidebar.multiselect('Search by Dungeon',df['Dungeon'].unique())

                if dungeon_search == []:
                    type_search = df['Dungeon'].unique()

                filter = df['Dungeon'].isin(type_search)
                df = df[filter]

                st.table(df)
        elif database_selection == 'leather_crafting':
                st.table(df)

    with st.expander('Give it to me Raw!'):
        query = st.text_input('Search', f'SELECT * FROM {database_selection}')
        df_results = pd.read_sql(query, conn)
        csv = df_results.to_csv(index=False)
        st.download_button('Download Results', data=csv, file_name='results.csv')
        st.table(df_results)