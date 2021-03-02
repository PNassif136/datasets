# Import modules
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly as ply
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px

st.title('Building Interactive Visualization with Streamlit')
st.write('Paul Nassif - ID# 201401003 :sunglasses:')

# Import first dataset by reading csv
cars = pd.read_csv('mtcars.csv')
st.subheader('Let\'s have a look around a popular car dealer\'s showroom:')

# Display dataframe by selecting button of choice
if st.button('Interested in the full range of cars for sale? – Press me!'):
    st.write(cars)

if st.button('TL;DR? – Press me for a selection of 5 cars in the showroom!'):
    st.write(cars.head(5))

# Bar Plot of MPG by Car Type
st.subheader('A car in this economy should be fuel-efficient!')
st.write('Scan the below Bar Plot to select the right car for you:')
fig = px.bar(cars, x= 'manufacturer', y= 'mpg')
fig.update_xaxes(type='category')
st.write(fig)

st.subheader('Let\'s topographically explore Mount Bruno\'s Elevation:')
elevation = pd.read_csv('mt_bruno_elevation.csv')

fig2 = go.Figure(data=[go.Surface(z= elevation.values)])
fig2.update_layout(autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))
st.write(fig2)

# Plotting interactive map of airport locations across the US
st.subheader('Ever wondered how many airports are located across the US?')
mapbox_access_token = 'pk.eyJ1IjoicG5hc3NpZjEzNiIsImEiOiJja2w0NHE5OGowYXZ0Mm9wNnM0M2Q5dDhvIn0.dc-zPUWQqfRIPYmBLuOLZw'

airport = pd.read_csv('airport.csv')
site_lat = airport.lat
site_lon = airport.lon
locations_name = airport.airport

data = [
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=17,
            color='rgb(255, 0, 0)',
            opacity=0.7
        ),
        text=locations_name,
        hoverinfo='text'
    ),
    go.Scattermapbox(
        lat=site_lat,
        lon=site_lon,
        mode='markers',
        marker=dict(
            size=8,
            color='rgb(242, 177, 172)',
            opacity=0.7
        ),
        hoverinfo='none'
    )]


layout = go.Layout(
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=3,
        style='light'
    ),
)

fig3 = dict(data=data, layout=layout)
st.write(fig3)

# Animated figure of number of passes per team/player per season (in minutes)
st.subheader('Check out the number of shots per player in a given season:')
football = pd.read_csv('football.csv')

fig4 = px.scatter(football, x="shots", y="minutes", animation_frame="position", animation_group="surname",
           size="shots", color="team", hover_name="surname")
st.write(fig4)
