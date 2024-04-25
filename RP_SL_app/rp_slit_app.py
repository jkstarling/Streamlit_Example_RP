import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Remedy Place - Streamlit Example Webpages", page_icon = "♾️" )

st.write("""
        # Remedy Place - Streamlit Example Webpages

        This website will highlight a handful of Streamlit possibilities that will help Remedy Place be financially sound.
        """)


# myfile = st.sidebar.file_uploader("RP_example_data_1-23_3_24.xlsx", type=["xlsx"])

df = pd.read_csv('G:\My Drive\kordis\Streamlit_Example_RP\RP_SL_app\RP_example_data_1-23_3_24.csv')

# if csvFile is not None:
# df = pd.read_csv(myfile)

# if "dataframe" not in st.session_state:
st.session_state["dataframe"] = df
st.dataframe(st.session_state.dataframe)
