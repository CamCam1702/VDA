import streamlit as st              
import pandas as pd                 
import numpy as np                  
import altair as alt                
import matplotlib.pyplot as plt     
import plotly.express as px         
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

dfBitcoin1 = pd.read_csv(r"D:\uet\K2N3\Data\BTL\Data\Bitcoin Historical Data6.csv")


dfBitcoin1['Date'] = pd.to_datetime(dfBitcoin1['Date'])

sdate = '2012-05-12'
edate = '2024-05-11'
mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 3 == 0)
dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

st.subheader('The Halving')
fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

specific_date_1 = '2020-05-12'
specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

bottom_date = '2014-04-10'
specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

traces = []

traces.append(go.Scatter(
        x=[specific_date_1],
        y=specific_price_1,
        mode='markers',
        marker=dict(size=10, color='magenta', symbol='circle'),
        name='Start day',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

traces.append(go.Scatter(
        x=[bottom_date],
        y=specific_price,
        mode='markers',
        marker=dict(size=10, color='magenta', symbol='circle'),
        name='Bottom',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

fig.add_traces(data=traces)

fig.update_layout(
            xaxis=dict(title='Date'),
            yaxis=dict(title='Price'),
            legend=dict(x=1.2, y=1)
        )

st.plotly_chart(fig, use_container_width=True)