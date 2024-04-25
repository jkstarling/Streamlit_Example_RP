import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from helper import get_route, get_map
st.set_page_config(page_title = "Cash Flow Statement", page_icon = "💵" )

start = st.text_input("Input the Starting Point")

stop = st.text_input("Input the End Point")



# Start by geocoding

if start and stop: 
    start = geopandas.tools.geocode(start)
    stop = geopandas.tools.geocode(stop)


    #Calculate route and plot on map
    route = get_route(start.geometry.x[0], 
                    start.geometry.y[0], 
                    stop.geometry.x[0], 
                    stop.geometry.y[0])
                    
    m = get_map(route, zoom = 9)

    st_data = folium_static(m)
                    # center = st.session_state['center'], 
                    # zoom = st.session_state['zoom'], 
                    # key = "new")
            #   center = [0,0], 
            #   width = 1200, 
            #   height = 500)

