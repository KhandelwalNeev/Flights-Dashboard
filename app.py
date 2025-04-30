import streamlit as st
from dbhelper import DB
import pandas as pd 
import plotly.graph_objects as go
import altair as alt


Flight = pd.DataFrame(columns = ['Airline' , 'Route' , 'Dep_Time' , 'Duration' , 'Total_Stops' , 'Price'])


db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu' , ['Select One' , 'Check Flights' , 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check FLights')
    
    col1 , col2 = st.columns(2)
    
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source' , sorted(city))
    
    with col2:
        destination = st.selectbox('Destination' , sorted(city))
        
    if st.button('Search'):
        results = db.fetch_all_flights(source , destination)
        
        if results:
            Flight = pd.DataFrame(results , columns = ['Airline' , 'Route' , 'Dep_Time' , 'Duration' , 'Total_Stops' , 'Price'])
            
        st.dataframe(Flight)
    
elif user_option == "Analytics":
    airline , frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels = airline,
            values = frequency,
            hoverinfo = 'label+percent',
            textinfo = 'value'
        )
    )
    st.header('Pie Chart')
    st.plotly_chart(fig)
    
    # bar chart for busiest airport 

    city , frequency = db.busy_airport()
    fig = go.Figure(
        go.Bar(
            x = city,
            y = frequency
        )
    ) 
    st.header('Bar Chart')
    st.plotly_chart(fig)    
    
    #  line chart for date of journey and frequency
    
    date , frequency = db.daily_frequency()
    fig = go.Figure(
        go.Scatter(
            mode = 'lines',
            x = date,
            y = frequency,
            line = dict(color = 'darkorchid')

        )
    )
    st.header('Line Chart')
    st.plotly_chart(fig)
        
else:
    st.title('Tell about the project.')