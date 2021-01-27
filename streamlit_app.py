import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in New York city")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns',inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

load_data_state = st.text('Loading data...')
data = load_data(10000)
load_data_state.text('Loading data successfull! USing st.cache')

st.subheader('Raw data')
st.write(data)

st.subheader('Number of pickups by hours')

hist_value = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_value)

st.subheader('Map of all pickups')
st.map(data)

#filter pickup by hour
#hour_to_filter = 17
hour_to_filter = st.slider('hour',0,23,17) #default 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


# Add a selectbox to the sidebar:
add_selectbox = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.beta_columns(2)
#you can use column just like sidebar
left_column.button('Press Me!')

#Or even better call fucntion with block
with right_column:
    choose = st.radio('Sorting hat',('Gryffinder','Ravenclaw','Hufflepuff','Styelen'))
    st.write(f'You are in {choose} house!')