import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


st.set_page_config(page_title = "Profit and Loss Statement", page_icon = "💰" )

df = st.session_state["dataframe"]

# df['date'] = pd.to_datetime(df['date'])
# df['date2'] = pd.to_datetime(df['date'], format='%b %Y').dt.to_period('M')

df_pl = df[df['report'].str.contains("PL")]
df_pl_membrev = df_pl[df_pl.rowname=='Membership Revenue']


pivot_table = pd.pivot_table(df_pl, 
                             index=('ind_row', 'rowname'), 
                             columns='date2', 
                             values='cost', 
                             aggfunc='sum', 
                             fill_value=0).reset_index()

st.write("""
        # Remedy Place - Profit and Loss Statements for all sub-companies.
        """)

# st.dataframe(pivot_table)
st.dataframe(pivot_table.drop('ind_row', axis=1))

fig = go.Figure()

# Assuming df_pl_membrev is your DataFrame and 'date' is in the "MMM-YY" format
df_pl_membrev['date'] = pd.to_datetime(df_pl_membrev['date'], format='%b-%y')

# Add a trace for each unique value in 'report'
for report_value in df_pl_membrev['report'].unique():
    df_report = df_pl_membrev[df_pl_membrev['report'] == report_value]
    fig.add_trace(go.Scatter(
        x=df_report['date'],
        y=df_report['cost'],
        mode='lines+markers',
        name=report_value,
        line=dict(width=2),
        marker=dict(size=8),
    ))

fig.update_layout(
    title='Membership Revenue by Location',
    xaxis_title='Date',
    yaxis_title='Revenue',
    xaxis_tickangle=-45,
    showlegend=True,
)

# Display the Plotly figure in Streamlit
st.plotly_chart(fig)
# fig.show()