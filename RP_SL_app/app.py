import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title = "Remedy Place - Streamlit Example Webpages", page_icon = "♾️" )

st.write("""
        # Remedy Place - Streamlit Example Webpages

        This website will highlight a handful of Streamlit possibilities for Remedy Place and others.
        """)
 

# myfile = st.sidebar.file_uploader("RP_example_data_1-23_3_24.xlsx", type=["xlsx"])

# os.chdir(r"G:/My Drive/kordis/SL_example/PythonStreamlit")
df = pd.read_csv('G:\My Drive\kordis\Streamlit_Example_RP\RP_SL_app\RP_example_data_1-23_3_24.csv')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
# Format 'date' as "MMM-YY"
# df['date'] = df['date'].dt.strftime('%b-%y')
df['date2'] = pd.to_datetime(df['date'], format='%b %Y').dt.to_period('M')

# if "dataframe" not in st.session_state:
st.session_state["dataframe"] = df

## show dataframe
# st.dataframe(st.session_state.dataframe)
