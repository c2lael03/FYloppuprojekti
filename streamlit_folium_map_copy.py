# Lopputehtava: Streamlit
# https://unioulu-my.sharepoint.com/personal/ilpovirt_oamk_fi/_layouts/15/stream.aspx?id=%2Fpersonal%2Filpovirt%5Foamk%5Ffi%2FDocuments%2FLuentojen%5Ftallenteet%2F2024%2D2025%2FSoveltava%5Fmatematiikka%5Fja%5Ffysiikka%2Fstreamlit%5FFI%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2Ed068eb43%2D5cbe%2D4363%2Db54b%2D88fd54481496

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
# import matplotlib.pyplot as plt
# import numpy as np

path = "Location.csv"
df = pd.read_csv(path)

st.title('Loppukavely')

# Print values
st.write("Keskinopeus on :", df['Speed (m/s)'].mean(), 'm/s' )
st.write("Kokonaismatka on :", df['Distance (km)'].max(), 'km' )

# Draw line plot
st.line_chart(df, x = 'Time (s)', y = 'Distance (km)', y_label = 'Distance', x_label = 'Time' )

#Create a map where the center is at start_lat start_long and zoom level is defined
start_lat = df['Latitude (°)'].mean()
start_long = df['Longitude (°)'].mean()
map = folium.Map(location = [start_lat, start_long], zoom_start = 14)

# Draw the map
folium.Polyline(df[['Latitude (°)','Longitude (°)']], color = 'blue', weight = 3.5, opacity = 1).add_to(map)

#Define map dimensions and show the map
st_map = st_folium(map, width=900, height=650)