import streamlit
import pandas as pd


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
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# display table on the page
streamlit.dataframe(my_fruit_list)




