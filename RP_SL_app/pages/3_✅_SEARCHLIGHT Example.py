import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
import warnings
from helper import *

warnings.filterwarnings('ignore')

st.set_page_config(page_title="Super Service", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Super Service")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

os.chdir(r"G:/My Drive/kordis/Streamlit_Example_RP/RP_SL_app/")
df_sl = pd.read_csv("searchlight_data.csv")#, encoding = "ISO-8859-1")

# df = pd.read_csv('G:\My Drive\kordis\Streamlit_Example_RP\RP_SL_app\RP_example_data_1-23_3_24.csv')

col1, col2 = st.columns([1,2])

with col1:

    with st.container():
        st.header('Effectiveness Metrics')

        for i in range(4):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            numb_print(mymetric, mynumb, myperc)

        st.divider()

        st.header('Efficiency Metrics')

        for i in range(4,7):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            perc_print(mymetric, mynumb, myperc)

        for i in range(7,9):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            dollar_print(mymetric, mynumb, myperc)


with col2:
    # data_df = pd.DataFrame(
    # {"sales": [ [0, 4, 26, 80, 100, 40],
    #         [80, 20, 80, 35, 40, 100],
    #         [10, 20, 80, 80, 70, 0],
    #         [10, 100, 20, 100, 30, 100]]} )
    rev_df = pd.DataFrame(
    {"revenue": [ [0, 4, 26, 80, 100, 40] ]} )
    sold_df = pd.DataFrame(
    {"sold": [ [80, 20, 80, 35, 40, 100] ]} )
    closed_df = pd.DataFrame(
    {"closed": [ [10, 20, 80, 80, 70, 0] ]} )

    c1, c2 = st.columns(2)
    with c1:
        for i in range(9,10):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            numb_print(mymetric, mynumb, myperc)
    with c2:
        for i in range(13,14):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            kdollar_print(mymetric, mynumb, myperc)

    st.divider()
    cc1, cc2 = st.columns(2)

    with cc1:
        for i in range(10,13):
            mymetric, mynumb, myperc = df_sl.iloc[i,:]
            kdollar_print(mymetric, mynumb, myperc)

    with cc2:
        st.data_editor(
            rev_df,
            column_config={
                "revenue": st.column_config.LineChartColumn(
                    "revenue",
                    width="medium",
                    # help="The sales volume in the last 6 months",
                    y_min=0, y_max=100,  ),   },  hide_index=True,    )

        st.data_editor(
            sold_df,
            column_config={
                "sold": st.column_config.LineChartColumn(
                    "sold",
                    width="medium",
                    # help="The sales volume in the last 6 months",
                    y_min=0, y_max=100,  ),   },  hide_index=True,    )
            
        st.data_editor(
            closed_df,
            column_config={
                "closed": st.column_config.LineChartColumn(
                    "closed",
                    width="medium",
                    help="The sales volume in the last 6 months",
                    y_min=0, y_max=100,  ),   },  hide_index=True)


# df_sl
    values = df_sl.iloc[10:13].value
    labels = ['Revenue', 'Sold', 'Closed']
    fig = go.Figure(go.Bar(
            x=values,
            y=labels,
            orientation='h', 
            text=[f'${val:.2f}K' for val in values]
        ))
    fig.update_layout(title='Horizontal Bar Chart Example')
    st.plotly_chart(fig)
    # st.subheader("Category wise Sales")
    # fig = px.bar(category_df, x = "Category", y = "Sales", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]],
    #              template = "seaborn")
    # st.plotly_chart(fig,use_container_width=True, height = 200)

# with col2:
#     st.subheader("Region wise Sales")
#     fig = px.pie(filtered_df, values = "Sales", names = "Region", hole = 0.5)
#     fig.update_traces(text = filtered_df["Region"], textposition = "outside")
#     st.plotly_chart(fig,use_container_width=True)

#     with c2:
#         st.data_editor(
#             data_df.iloc[:2,:],
#             column_config={
#                 "sales": st.column_config.LineChartColumn(
#                     # "Sales (last 6 months)",
#                     width="medium",
#                     # help="The sales volume in the last 6 months",
#                     y_min=0,
#                     y_max=100,
#                 ),
#             },
#             hide_index=True,
#         )



# linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
# fig2 = px.line(linechart, x = "month_year", y="Sales", labels = {"Sales": "Amount"},height=500, width = 1000,template="gridon")
# st.plotly_chart(fig2,use_container_width=True)



# chart1, chart2 = st.columns((2))
# with chart1:
#     st.subheader('Segment wise Sales')
#     fig = px.pie(filtered_df, values = "Sales", names = "Segment", template = "plotly_dark")
#     fig.update_traces(text = filtered_df["Segment"], textposition = "inside")
#     st.plotly_chart(fig,use_container_width=True)

# with chart2:
#     st.subheader('Category wise Sales')
#     fig = px.pie(filtered_df, values = "Sales", names = "Category", template = "gridon")
#     fig.update_traces(text = filtered_df["Category"], textposition = "inside")
#     st.plotly_chart(fig,use_container_width=True)

# import plotly.figure_factory as ff
# st.subheader(":point_right: Month wise Sub-Category Sales Summary")
# with st.expander("Summary_Table"):
#     df_sample = df[0:5][["Region","State","City","Category","Sales","Profit","Quantity"]]
#     fig = ff.create_table(df_sample, colorscale = "Cividis")
#     st.plotly_chart(fig, use_container_width=True)

#     st.markdown("Month wise sub-Category Table")
#     filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
#     sub_category_Year = pd.pivot_table(data = filtered_df, values = "Sales", index = ["Sub-Category"],columns = "month")
#     st.write(sub_category_Year.style.background_gradient(cmap="Blues"))

# # Create a scatter plot
# data1 = px.scatter(filtered_df, x = "Sales", y = "Profit", size = "Quantity")
# data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
#                        titlefont = dict(size=20),xaxis = dict(title="Sales",titlefont=dict(size=19)),
#                        yaxis = dict(title = "Profit", titlefont = dict(size=19)))
# st.plotly_chart(data1,use_container_width=True)


