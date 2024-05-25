import streamlit as st
import folium
from streamlit_folium import st_folium

# Vytvoření základní mapy České republiky
m = folium.Map(location=[49.8175, 15.4730], zoom_start=7)

# Případné přidání markerů
folium.Marker([50.0755, 14.4378], popup='Praha').add_to(m)
folium.Marker([49.1951, 16.6068], popup='Brno').add_to(m)

# Vykreslení mapy pomocí st_folium
st_folium(m, width=700, height=500)