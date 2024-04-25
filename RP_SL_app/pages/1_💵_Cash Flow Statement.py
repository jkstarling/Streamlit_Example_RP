import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title = "Cash Flow Statement", page_icon = "💵" )

df = st.session_state["dataframe"]




if "dataframe" in st.session_state:
    st.table(st.session_state["dataframe"])



