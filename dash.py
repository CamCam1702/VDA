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
mask = (
    (dfBitcoin1['Date'] >= sdate) &
    (dfBitcoin1['Date'] <= edate) &
    (dfBitcoin1['Date'].dt.day % 3 == 0) 
)
dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

place = st.sidebar.radio('', ['Halving', 'Halving number 1', 'Halving number 2', 'Halving number 3', 'Presidents', 'War', 'Covid', 'China', 'Hack'])
if place == 'Presidents':

    start_date = '2020-10-03'
    end_date = '2020-12-03'
    date = '2020-11-03'

    mask = (dfBitcoin1['Date'] >= start_date) & (dfBitcoin1['Date'] <= end_date) & (dfBitcoin1['Date'].dt.day % 3 == 0)
    dfBitcoin1_40_america = dfBitcoin1.loc[mask]
    mask2 = (dfBitcoin1['Date'] >= start_date) & (dfBitcoin1['Date'] <= end_date)
    dfBitcoin1_40_america_2 =dfBitcoin1.loc[mask2]



    traces = []

    dfBitcoin1_40_america_2['Change %'] = dfBitcoin1_40_america_2['Change %'].str.rstrip('%').astype(float)

    df_new = pd.DataFrame({
        'period': ['Before', 'After'],
        'avg_change': [
            dfBitcoin1_40_america_2[dfBitcoin1_40_america_2['Date'] < date]['Change %'].sum(),
            dfBitcoin1_40_america_2[dfBitcoin1_40_america_2['Date'] > date]['Change %'].sum()
        ]
    })

    # Tạo trace cho đoạn trước năm 2010
    traces.append(go.Scatter(
            x=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] < '2020-11-04']['Date'],
            y=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] < '2020-11-04']['Price'],
            mode='lines',
            line=dict(color='red'),  # Màu xanh cho đoạn trước 2010
            name='Before presidential election',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

        # Tạo trace cho đoạn sau năm 2011
    traces.append(go.Scatter(
            x=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] > '2020-11-01']['Date'],
            y=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] > '2020-11-01']['Price'],
            mode='lines',
            line=dict(color='blue'),  # Màu xanh cho đoạn sau 2011
            name='After presidential election',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

        # Tạo figure và thêm các trace
    fig = go.Figure(data=traces)

        # Thiết lập layout cho figure
    fig.update_layout(template="gridon",legend=dict(x=0, y=1),xaxis=dict(title='Date'),
            yaxis=dict(title='Price'))

    st.subheader("Price of bitcoin in 2020 presidential election ")
    col1, col2 = st.columns((1.8,1))
    with col1:
    
        st.plotly_chart(fig,use_container_width=True)


    fig = px.bar(df_new, x='period', y='avg_change', color='period',
                labels={'avg_change': 'Average Change %', 'period': 'Period'},
                title='Average Change %')

        # Customize layout
    fig.update_layout(
            xaxis=dict(title='Period'),
            yaxis=dict(title='Average Change %'),
            template='plotly_dark',  # Choose a plotly template
            legend=dict(x=1.2, y=1)
        )

        # Display the chart in Streamlit
    with col2:
        st.plotly_chart(fig, use_container_width=True)


    start_date = '2016-09-03'
    end_date = '2016-12-31'
    date = '2016-11-08'

    mask = (dfBitcoin1['Date'] >= start_date) & (dfBitcoin1['Date'] <= end_date) & (dfBitcoin1['Date'].dt.day % 3 == 0)
    dfBitcoin1_40_america = dfBitcoin1.loc[mask]
    mask2 = (dfBitcoin1['Date'] >= start_date) & (dfBitcoin1['Date'] <= end_date)
    dfBitcoin1_40_america_2 =dfBitcoin1.loc[mask2]

    traces = []

    dfBitcoin1_40_america_2['Change %'] = dfBitcoin1_40_america_2['Change %'].str.rstrip('%').astype(float)

    df_new = pd.DataFrame({
        'period': ['Before', 'After'],
        'avg_change': [
            dfBitcoin1_40_america_2[dfBitcoin1_40_america_2['Date'] < date]['Change %'].sum(),
            dfBitcoin1_40_america_2[dfBitcoin1_40_america_2['Date'] > date]['Change %'].sum()
        ]
    })

    # Tạo trace cho đoạn trước năm 2010
    traces.append(go.Scatter(
            x=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] < '2016-11-04']['Date'],
            y=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] < '2016-11-04']['Price'],
            mode='lines',
            line=dict(color='red'),  # Màu xanh cho đoạn trước 2010
            name='Before presidential election',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

        # Tạo trace cho đoạn sau năm 2011
    traces.append(go.Scatter(
            x=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] > '2016-11-01']['Date'],
            y=dfBitcoin1_40_america[dfBitcoin1_40_america['Date'] > '2016-11-01']['Price'],
            mode='lines',
            line=dict(color='blue'),  # Màu xanh cho đoạn sau 2011
            name='After presidential election',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

        # Tạo figure và thêm các trace
    fig = go.Figure(data=traces)

        # Thiết lập layout cho figure
    fig.update_layout(template="gridon",legend=dict(x=0, y=1))

    st.subheader("Price of bitcoin in 2016 presidential election ")
    col1, col2 = st.columns((1.8,1))
    with col1:
        
        st.plotly_chart(fig,use_container_width=True)


    fig = px.bar(df_new, x='period', y='avg_change', color='period',
                labels={'avg_change': 'Average Change %', 'period': 'Period'},
                title='Average Change %')

        # Customize layout
    fig.update_layout(
            xaxis=dict(title='Period'),
            yaxis=dict(title='Average Change %'),
            template='plotly_dark',  # Choose a plotly template
            legend=dict(x=1, y=1)
        )

        # Display the chart in Streamlit
    with col2:
        st.plotly_chart(fig, use_container_width=True)

elif place == 'War':
    start_date_1 = '2022-01-01'
    end_date_2 = '2022-04-30'
    mask_3 = (dfBitcoin1['Date'] >= start_date_1) & (dfBitcoin1['Date'] <= end_date_2) & (dfBitcoin1['Date'].dt.day % 4 == 0)
    dfBitcoin1_40 = dfBitcoin1.loc[mask_3]

    st.subheader('Will the Russia-Ukraine War Affect Bitcoin Price ?')
    traces = []
    # Tạo trace cho đoạn trong chiến tranh
    traces.append(go.Scatter(
        x=dfBitcoin1_40[(dfBitcoin1_40['Date'] >= '2022-02-24') & (dfBitcoin1_40['Date'] <= '2022-03-28')]['Date'],
        y=dfBitcoin1_40[(dfBitcoin1_40['Date'] >= '2022-02-24') & (dfBitcoin1_40['Date'] <= '2022-03-28')]['Price'],
        mode='lines',
        line=dict(color='red'),  # Màu đỏ cho đoạn từ 2010 đến 2011
        name='War started',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    # Tạo trace cho đoạn trước năm 2010
    traces.append(go.Scatter(
        x=dfBitcoin1_40[dfBitcoin1_40['Date'] < '2022-02-25']['Date'],
        y=dfBitcoin1_40[dfBitcoin1_40['Date'] < '2022-02-25']['Price'],
        mode='lines',
        line=dict(color='blue'),  # Màu xanh cho đoạn trước 2010
        name='',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    # Tạo trace cho đoạn sau năm 2011
    traces.append(go.Scatter(
        x=dfBitcoin1_40[dfBitcoin1_40['Date'] > '2022-03-26']['Date'],
        y=dfBitcoin1_40[dfBitcoin1_40['Date'] > '2022-03-26']['Price'],
        mode='lines',
        line=dict(color='blue'),  # Màu xanh cho đoạn sau 2011
        name='',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    specific_date_1 = '2022-03-28'
    specific_price_1 = dfBitcoin1_40[dfBitcoin1_40['Date'] == '2022-03-28']['Price']
    traces.append(go.Scatter(
        x=[specific_date_1],
        y=specific_price_1,
        mode='markers',
        marker=dict(size=10, color='magenta', symbol='circle'),
        name='SWIFT',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    # Tạo figure và thêm các trace
    fig = go.Figure(data=traces)

    # Thiết lập layout cho figure
    fig.update_layout(template="gridon", xaxis=dict(title='Date'),
            yaxis=dict(title='Price'))

    # Hiển thị biểu đồ
    st.plotly_chart(fig, use_container_width=True)

elif place == 'Halving' :
    st.subheader('The Halving')
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2012-11-27'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    specific_date_2 = '2016-07-09'
    specific_price_2 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_2]['Price']

    specific_date_3 = '2020-05-12'
    specific_price_3 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_3]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='magenta', symbol='circle'),
            name='The first halving',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    traces.append(go.Scatter(
            x=[specific_date_2],
            y=specific_price_2,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='The second halving',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[specific_date_3],
            y=specific_price_3,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='The third halving',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

elif place == 'Covid':
    sdate = '2019-10-20'
    edate = '2022-01-30'
    mask_3 = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate)  & (dfBitcoin1['Date'].dt.day % 4 == 0)
    dfBitcoin1_covid = dfBitcoin1.loc[mask_3]

    st.subheader('How covid-19 affect to bitcoin?')
    traces = []
    traces.append(go.Scatter(
        x=dfBitcoin1_covid[dfBitcoin1_covid['Date'] < '2019-12-25']['Date'],
        y=dfBitcoin1_covid[dfBitcoin1_covid['Date'] < '2019-12-25']['Price'],
        mode='lines',
        line=dict(color='blue'),
        name=None,
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    traces.append(go.Scatter(
        x=dfBitcoin1_covid[dfBitcoin1_covid['Date'] > '2020-05-27']['Date'],
        y=dfBitcoin1_covid[dfBitcoin1_covid['Date'] > '2020-05-27']['Price'],
        mode='lines',
        line=dict(color='blue'),
        name=None,
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>',
    ))

    traces.append(go.Scatter(
        x=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2019-12-24') & (dfBitcoin1_covid['Date'] <= '2020-06-01')]['Date'],
        y=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2019-12-24') & (dfBitcoin1_covid['Date'] <= '2020-06-01')]['Price'],
        mode='lines',
        line=dict(color='red'),
        name='The first wave of COVID',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    traces.append(go.Scatter(
        x=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2020-12-24') & (dfBitcoin1_covid['Date'] <= '2021-02-01')]['Date'],
        y=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2020-12-24') & (dfBitcoin1_covid['Date'] <= '2021-02-01')]['Price'],
        mode='lines',
        line=dict(color='lavender'),
        name='The second wave of COVID',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    traces.append(go.Scatter(
        x=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2021-04-01') & (dfBitcoin1_covid['Date'] <= '2021-06-01')]['Date'],
        y=dfBitcoin1_covid[(dfBitcoin1_covid['Date'] >= '2021-04-01') & (dfBitcoin1_covid['Date'] <= '2021-06-01')]['Price'],
        mode='lines',
        line=dict(color='green'),
        name='The time Delta variant arived',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    specific_date = '2019-12-28'
    specific_price = dfBitcoin1_covid[dfBitcoin1_covid['Date'] == '2019-12-28']['Price']
    traces.append(go.Scatter(
        x=[specific_date],
        y=specific_price,
        mode='markers',
        marker=dict(size=10, color='magenta', symbol='circle'),
        name='The day covid start',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    specific_date_1 = '2020-03-04'
    specific_price_1 = dfBitcoin1_covid[dfBitcoin1_covid['Date'] == '2020-03-04']['Price']
    traces.append(go.Scatter(
        x=[specific_date_1],
        y=specific_price_1,
        mode='markers',
        marker=dict(size=10, color='gold', symbol='circle'),
        name='The day WHO announce',
        hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    ))

    fig = go.Figure(data=traces)

    fig.update_layout(template="gridon", xaxis=dict(title='Date'),
            yaxis=dict(title='Price'))
    st.plotly_chart(fig, use_container_width=True)

elif place == 'Halving number 1':
    sdate = '2012-05-12'
    edate = '2016-07-09'
    mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 3 == 0)
    dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

    st.subheader('Halving number 1')
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2012-05-12'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    bottom_date = '2014-02-21'
    specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

    High_date = '2013-11-30'
    specific_hprice = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == High_date]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Start day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    traces.append(go.Scatter(
            x=[bottom_date],
            y=specific_price,
            mode='markers',
            marker=dict(size=10, color='magenta', symbol='circle'),
            name='Bottom day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[High_date],
            y=specific_hprice,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='Peak day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

elif place == 'Halving number 2':
    sdate = '2016-07-09'
    edate = '2020-05-11'
    mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 3 == 0)
    dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

    st.subheader('Halving number 2')
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2016-07-09'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    bottom_date = '2018-04-06'
    specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

    High_date = '2017-12-18'
    specific_hprice = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == High_date]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Start day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    traces.append(go.Scatter(
            x=[bottom_date],
            y=specific_price,
            mode='markers',
            marker=dict(size=10, color='magenta', symbol='circle'),
            name='Bottom day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[High_date],
            y=specific_hprice,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='Peak day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

elif place == 'Halving number 3':
    sdate = '2020-05-12'
    edate = '2024-04-19'
    mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 3 == 0)
    dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

    st.subheader('Halving number 3')
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2020-05-12'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    bottom_date = '2021-07-18'
    specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

    High_date = '2024-03-12'
    specific_hprice = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == High_date]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Start day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    # traces.append(go.Scatter(
    #         x=[bottom_date],
    #         y=specific_price,
    #         mode='markers',
    #         marker=dict(size=10, color='magenta', symbol='circle'),
    #         name='Bottom day',
    #         hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
    #     ))
    
    traces.append(go.Scatter(
            x=[High_date],
            y=specific_hprice,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='Peak day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

elif place == 'Hack':
    sdate = '2014-02-02'
    edate = '2014-05-01'
    mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 1 == 0)
    dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

    st.subheader("Impact of the Mt. Gox Hack on Bitcoin Price (February 2014)")
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2014-02-28'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    specific_date_2 = '2014-02-05'
    specific_price_2 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_2]['Price']

    bottom_date = '2014-04-10'
    specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Bankrupt day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[specific_date_2],
            y=specific_price_2,
            mode='markers',
            marker=dict(size=10, color='magenta', symbol='circle'),
            name='Start day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[bottom_date],
            y=specific_price,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='Bottom day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

else :
    sdate = '2021-05-10'
    edate = '2021-06-19'
    mask = (dfBitcoin1['Date'] >= sdate) & (dfBitcoin1['Date'] <= edate) & (dfBitcoin1['Date'].dt.day % 2 == 0)
    dfBitcoin1_halving_1 = dfBitcoin1.loc[mask]

    st.subheader("Impact of China's Cryptocurrency Crackdown on Bitcoin Price")
    fig = px.line(dfBitcoin1_halving_1, x = 'Date', y= 'Price')

    specific_date_1 = '2021-05-14'
    specific_price_1 = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == specific_date_1]['Price']

    bottom_date = '2021-06-08'
    specific_price = dfBitcoin1_halving_1[dfBitcoin1_halving_1['Date'] == bottom_date]['Price']

    traces = []

    traces.append(go.Scatter(
            x=[specific_date_1],
            y=specific_price_1,
            mode='markers',
            marker=dict(size=10, color='red', symbol='circle'),
            name='Start day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))
    
    traces.append(go.Scatter(
            x=[bottom_date],
            y=specific_price,
            mode='markers',
            marker=dict(size=10, color='gold', symbol='circle'),
            name='Bottom day',
            hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> %{y}<extra></extra>'
        ))

    fig.add_traces(data=traces)

    fig.update_layout(
                xaxis=dict(title='Date'),
                yaxis=dict(title='Price'),
                legend=dict(x=1.2, y=1)
            )

    st.plotly_chart(fig, use_container_width=True)

