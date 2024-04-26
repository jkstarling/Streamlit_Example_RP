import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(page_title = "Cash Flow Statement", page_icon = "💵" )

df = st.session_state["dataframe"]

# df['date'] = pd.to_datetime(df['date'])
# df['date2'] = pd.to_datetime(df['date'], format='%b %Y').dt.to_period('M')

df_cf = df[df['report'].str.contains("Total CF")]
df_cf_netincome = df_cf[df_cf.rowname=='Net Income']


pivot_table = pd.pivot_table(df_cf, 
                             index=('ind_row', 'rowname'), 
                             columns='date2', 
                             values='cost', 
                             aggfunc='sum', 
                             fill_value=0).reset_index()

st.write("""
        # Remedy Place - Total Cash Flow for all sub-companies.
        """)

# st.dataframe(pivot_table)
st.dataframe(pivot_table.drop('ind_row', axis=1))


# Create Plotly figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_cf_netincome.date, y=df_cf_netincome.cost, mode='lines+markers', name='Net Income'))
fig.update_layout(title='Net Income Over Time',
                  xaxis_title='Date',
                  yaxis_title='Net Income',
                  xaxis_tickangle=-45,
                  showlegend=True)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)