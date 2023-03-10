#import pandas
#import streamlit
#import requests
#import snowflake.connector
#from urllib.error import URLError

#streamlit.title('My parents New Healthy Diner')
#streamlit.header("🥑Breakfast Menu🍞")
#streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
#streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")
#streamlit.text("🐔 Hard-boiled Free-Range Egg")
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas 
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)

#Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])

#fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]

#streamlit.dataframe(fruits_to_show)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#streamlit.header("Fruityvice Fruit Advice!")

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
#streamlit.text(fruityvice_response.json())


# rite your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)


#streamlit.header("Fruityvice Fruit Advice!")
#try:

 #if not fruit_choice:
  #streamlit.error("Please select a fruit to get information.")
  #else:
   #back_from_function = get_fruitvice_data(fruit_choice)
    #treamlit.dataframe(back_from_function) 
      
#except URLError as e:
 # streamlit.error()
    
    
#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#streamlit.write('The user entered ', fruit_choice)

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.stop()

#import snowflake.connector 

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#add_my_fruit = streamlit.text_input("What fruit would you like to add?")

#streamlit.write('Thanks for adding ',add_my_fruit)

#my_cur.execute("insert into fruit_load_list values('from streamlit')")

import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents New Healthy Diner")
streamlit.header("🥑Breakfast Menu🍞")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-Range Egg")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruitvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()



streamlit.header("The fruit load list contains:")
#snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

#add button to laod the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
 

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
        return "Thanks for adding " + new_fruit
    
add_my_fruit = streamlit.text_input("What fruit would you like to add?")
if streamlit.button("Add a fruit to the list"):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)





streamlit.stop()

