import streamlit
import pandas as pd
import requests

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞 Acovado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# set index to fruit names so that our multi-select makes sense!
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding a pick list here so people can pick the fruit they want to include
# pre-populate the list, so that it is more obvious to customers
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display table on the page
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# make data readable
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# create data frame
streamlit.dataframe(fruityvice_normalized)

