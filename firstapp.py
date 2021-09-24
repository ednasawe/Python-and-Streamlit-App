# Creating my first Streamlit app

import streamlit as st
import numpy as np
import pandas as pd

# Adding a title to my first streamlit app

st.title("My first app")

# Writing andDisplaying a data frame to my first streamlit app
st.write(" Using data")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df 

# Drawing charts on my first streamlit app

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c'])

st.line_chart(chart_data)

# Plotting a map on my first streamlit app

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns = ['lat', 'lon'])

st.map(map_data)

# Adding widget for interactivity to my app

if st.checkbox('Show the dataframe'):
    chart_data = pd. DataFrame(
        np.random.randn(20, 3),
        columns = ['a', 'b', 'c'])
        
chart_data

 # Using a selectbox for options
option = st.selectbox(
    'Which is your favorite number?',
    df['first column'])

'You selected: ', option

# Laying out the app
#option = st.sidebar.selectbox(
    #'Which is your favorite number?',
  #  df['first column'])

#'You selected: ', option


left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")


# Showing progress of the app
# Importing time
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'



