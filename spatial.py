import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pydeck as pdk
from pylab import *
from palettable.cartocolors.sequential import BrwnYl_3

st.set_page_config(page_title='PVWatts Average', page_icon='📊')
st.title('📊Spatial analyzer of rooftop solar potential USA🇺🇸')

#CSV Files of Different Locations
df= pd.read_csv('brookhaven.csv')
df_w = pd.read_csv('cheyenne.csv')
df_m = pd.read_csv('miami.csv')
df_s = pd.read_csv('san diego.csv')
df_se = pd.read_csv('seattle.csv')
city = pd.read_csv('Cities.csv', usecols=['Latitude', 'Longitude', 'PVWatts'])
cities = ['Brookhaven', 'Cheyenne', 'Miami','San Diego', 'Seattle']

#Formatting of the GUI Application
with st.sidebar.subheader('Data'):
    box = st.selectbox(label ='Choose cities to compare: ', options = cities)
with st.sidebar.subheader('Data'):
    while(box in cities):
        cities.remove(box)
    box2 = st.selectbox('Choose second city:', options = cities)
with st.sidebar.header("Please Filter Here:"):
    st.title('Decide on a Month ')
    month = st.slider('Select a Month', 
                  min_value=1,
                  max_value=12,
                  )
with st.sidebar.subheader("Month selected is"):
    if month == 1:
        st.write('Displaying Results in January ☃️')
    elif month == 2:
        st.write('Displaying Results in February 💝' )
    elif month == 3:
        st.write('Displaying Results in March 🌈')
    elif month == 4:
        st.write('Displaying Results in April 🐝')
    elif month == 5:
        st.write('Displaying Results in May 🌸')
    elif month == 6:
        st.write('Displaying Results in June 🌇')
    elif month == 7:
        st.write('Displaying Results in July 🌻')
    elif month == 8:
        st.write('Displaying Results in August 🌼')
    elif month == 9:
        st.write('Displaying Results in September 🍁')
    elif month == 10:
        st.write('Displaying Results in October 🎃')
    elif month == 11:
        st.write('Displaying Results in November 🍂')
    elif month == 12:
        st.write('Displaying Results in December ❄️')

#Analysis Functions
def dc_array_output():
    hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    #The DC Array Output Lists for Diffeerent Locations
    output = []
    output_w = []
    output_m = []
    output_s = []
    output_se = []
    #Brookhaven Averages
    data = df[(df['Month'] == month) & (df['Hour'] == 0)]
    data_1 = df[(df['Month'] == month) & (df['Hour'] == 1)]
    data_2 = df[(df['Month'] == month) & (df['Hour'] == 2)]
    data_3 = df[(df['Month'] == month) & (df['Hour'] == 3)]
    data_4 = df[(df['Month'] == month) & (df['Hour'] == 4)]
    data_5 = df[(df['Month'] == month) & (df['Hour'] == 5)]
    data_6 = df[(df['Month'] == month) & (df['Hour'] == 6)]
    data_7 = df[(df['Month'] == month) & (df['Hour'] == 7)]
    data_8 = df[(df['Month'] == month) & (df['Hour'] == 8)]
    data_9 = df[(df['Month'] == month) & (df['Hour'] == 9)]
    data_10 = df[(df['Month'] == month) & (df['Hour'] == 10)]
    data_11 = df[(df['Month'] == month) & (df['Hour'] == 11)]
    data_12 = df[(df['Month'] == month) & (df['Hour'] == 12)]
    data_13 = df[(df['Month'] == month) & (df['Hour'] == 13)]
    data_14 = df[(df['Month'] == month) & (df['Hour'] == 14)]
    data_15 = df[(df['Month'] == month) & (df['Hour'] == 15)]
    data_16 = df[(df['Month'] == month) & (df['Hour'] == 16)]
    data_17 = df[(df['Month'] == month) & (df['Hour'] == 17)]
    data_18 = df[(df['Month'] == month) & (df['Hour'] == 18)]
    data_19 = df[(df['Month'] == month) & (df['Hour'] == 19)]
    data_20 = df[(df['Month'] == month) & (df['Hour'] == 20)]
    data_21 = df[(df['Month'] == month) & (df['Hour'] == 21)]
    data_22 = df[(df['Month'] == month) & (df['Hour'] == 22)]
    data_23 = df[(df['Month'] == month) & (df['Hour'] == 23)]

    output.append(data['DC Array Output (W)'].mean())
    output.append(data_1['DC Array Output (W)'].mean())
    output.append(data_2['DC Array Output (W)'].mean())
    output.append(data_3['DC Array Output (W)'].mean())
    output.append(data_4['DC Array Output (W)'].mean())
    output.append(data_5['DC Array Output (W)'].mean())
    output.append(data_6['DC Array Output (W)'].mean())
    output.append(data_7['DC Array Output (W)'].mean())
    output.append(data_8['DC Array Output (W)'].mean())
    output.append(data_9['DC Array Output (W)'].mean())
    output.append(data_10['DC Array Output (W)'].mean())
    output.append(data_11['DC Array Output (W)'].mean())
    output.append(data_12['DC Array Output (W)'].mean())
    output.append(data_13['DC Array Output (W)'].mean())
    output.append(data_14['DC Array Output (W)'].mean())
    output.append(data_15['DC Array Output (W)'].mean())
    output.append(data_16['DC Array Output (W)'].mean())
    output.append(data_17['DC Array Output (W)'].mean())
    output.append(data_18['DC Array Output (W)'].mean())
    output.append(data_19['DC Array Output (W)'].mean())
    output.append(data_20['DC Array Output (W)'].mean())
    output.append(data_21['DC Array Output (W)'].mean())
    output.append(data_22['DC Array Output (W)'].mean())
    output.append(data_23['DC Array Output (W)'].mean())

    #Wyoming Averages
    data_w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 0)]
    data_1w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 1)]
    data_2w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 2)]
    data_3w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 3)]
    data_4w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 4)]
    data_5w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 5)]
    data_6w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 6)]
    data_7w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 7)]
    data_8w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 8)]
    data_9w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 9)]
    data_10w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 10)]
    data_11w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 11)]
    data_12w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 12)]
    data_13w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 13)]
    data_14w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 14)]
    data_15w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 15)]
    data_16w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 16)]
    data_17w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 17)]
    data_18w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 18)]
    data_19w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 19)]
    data_20w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 20)]
    data_21w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 21)]
    data_22w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 22)]
    data_23w = df_w[(df_w['Month'] == month) & (df_w['Hour'] == 23)]

    output_w.append(data_w['DC Array Output (W)'].mean())
    output_w.append(data_1w['DC Array Output (W)'].mean())
    output_w.append(data_2w['DC Array Output (W)'].mean())
    output_w.append(data_3w['DC Array Output (W)'].mean())
    output_w.append(data_4w['DC Array Output (W)'].mean())
    output_w.append(data_5w['DC Array Output (W)'].mean())
    output_w.append(data_6w['DC Array Output (W)'].mean())
    output_w.append(data_7w['DC Array Output (W)'].mean())
    output_w.append(data_8w['DC Array Output (W)'].mean())
    output_w.append(data_9w['DC Array Output (W)'].mean())
    output_w.append(data_10w['DC Array Output (W)'].mean())
    output_w.append(data_11w['DC Array Output (W)'].mean())
    output_w.append(data_12w['DC Array Output (W)'].mean())
    output_w.append(data_13w['DC Array Output (W)'].mean())
    output_w.append(data_14w['DC Array Output (W)'].mean())
    output_w.append(data_15w['DC Array Output (W)'].mean())
    output_w.append(data_16w['DC Array Output (W)'].mean())
    output_w.append(data_17w['DC Array Output (W)'].mean())
    output_w.append(data_18w['DC Array Output (W)'].mean())
    output_w.append(data_19w['DC Array Output (W)'].mean())
    output_w.append(data_20w['DC Array Output (W)'].mean())
    output_w.append(data_21w['DC Array Output (W)'].mean())
    output_w.append(data_22w['DC Array Output (W)'].mean())
    output_w.append(data_23w['DC Array Output (W)'].mean())
    #Miami Averages
    data_m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 0)]
    data_1m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 1)]
    data_2m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 2)]
    data_3m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 3)]
    data_4m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 4)]
    data_5m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 5)]
    data_6m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 6)]
    data_7m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 7)]
    data_8m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 8)]
    data_9m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 9)]
    data_10m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 10)]
    data_11m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 11)]
    data_12m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 12)]
    data_13m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 13)]
    data_14m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 14)]
    data_15m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 15)]
    data_16m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 16)]
    data_17m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 17)]
    data_18m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 18)]
    data_19m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 19)]
    data_20m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 20)]
    data_21m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 21)]
    data_22m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 22)]
    data_23m = df_m[(df_m['Month'] == month) & (df_m['Hour'] == 23)]

    output_m.append(data_m['DC Array Output (W)'].mean())
    output_m.append(data_1m['DC Array Output (W)'].mean())
    output_m.append(data_2m['DC Array Output (W)'].mean())
    output_m.append(data_3m['DC Array Output (W)'].mean())
    output_m.append(data_4m['DC Array Output (W)'].mean())
    output_m.append(data_5m['DC Array Output (W)'].mean())
    output_m.append(data_6m['DC Array Output (W)'].mean())
    output_m.append(data_7m['DC Array Output (W)'].mean())
    output_m.append(data_8m['DC Array Output (W)'].mean())
    output_m.append(data_9m['DC Array Output (W)'].mean())
    output_m.append(data_10m['DC Array Output (W)'].mean())
    output_m.append(data_11m['DC Array Output (W)'].mean())
    output_m.append(data_12m['DC Array Output (W)'].mean())
    output_m.append(data_13m['DC Array Output (W)'].mean())
    output_m.append(data_14m['DC Array Output (W)'].mean())
    output_m.append(data_15m['DC Array Output (W)'].mean())
    output_m.append(data_16m['DC Array Output (W)'].mean())
    output_m.append(data_17m['DC Array Output (W)'].mean())
    output_m.append(data_18m['DC Array Output (W)'].mean())
    output_m.append(data_19m['DC Array Output (W)'].mean())
    output_m.append(data_20m['DC Array Output (W)'].mean())
    output_m.append(data_21m['DC Array Output (W)'].mean())
    output_m.append(data_22m['DC Array Output (W)'].mean())
    output_m.append(data_23m['DC Array Output (W)'].mean())
    #San Diego
    data_s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 0)]
    data_1s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 1)]
    data_2s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 2)]
    data_3s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 3)]
    data_4s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 4)]
    data_5s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 5)]
    data_6s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 6)]
    data_7s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 7)]
    data_8s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 8)]
    data_9s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 9)]
    data_10s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 10)]
    data_11s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 11)]
    data_12s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 12)]
    data_13s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 13)]
    data_14s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 14)]
    data_15s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 15)]
    data_16s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 16)]
    data_17s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 17)]
    data_18s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 18)]
    data_19s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 19)]
    data_20s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 20)]
    data_21s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 21)]
    data_22s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 22)]
    data_23s = df_s[(df_s['Month'] == month) & (df_s['Hour'] == 23)]

    output_s.append(data_s['DC Array Output (W)'].mean())
    output_s.append(data_1s['DC Array Output (W)'].mean())
    output_s.append(data_2s['DC Array Output (W)'].mean())
    output_s.append(data_3s['DC Array Output (W)'].mean())
    output_s.append(data_4s['DC Array Output (W)'].mean())
    output_s.append(data_5s['DC Array Output (W)'].mean())
    output_s.append(data_6s['DC Array Output (W)'].mean())
    output_s.append(data_7s['DC Array Output (W)'].mean())
    output_s.append(data_8s['DC Array Output (W)'].mean())
    output_s.append(data_9s['DC Array Output (W)'].mean())
    output_s.append(data_10s['DC Array Output (W)'].mean())
    output_s.append(data_11s['DC Array Output (W)'].mean())
    output_s.append(data_12s['DC Array Output (W)'].mean())
    output_s.append(data_13s['DC Array Output (W)'].mean())
    output_s.append(data_14s['DC Array Output (W)'].mean())
    output_s.append(data_15s['DC Array Output (W)'].mean())
    output_s.append(data_16s['DC Array Output (W)'].mean())
    output_s.append(data_17s['DC Array Output (W)'].mean())
    output_s.append(data_18s['DC Array Output (W)'].mean())
    output_s.append(data_19s['DC Array Output (W)'].mean())
    output_s.append(data_20s['DC Array Output (W)'].mean())
    output_s.append(data_21s['DC Array Output (W)'].mean())
    output_s.append(data_22s['DC Array Output (W)'].mean())
    output_s.append(data_23s['DC Array Output (W)'].mean())
    #Seattle Averages
    data_se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 0)]
    data_1se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 1)]
    data_2se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 2)]
    data_3se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 3)]
    data_4se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 4)]
    data_5se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 5)]
    data_6se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 6)]
    data_7se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 7)]
    data_8se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 8)]
    data_9se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 9)]
    data_10se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 10)]
    data_11se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 11)]
    data_12se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 12)]
    data_13se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 13)]
    data_14se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 14)]
    data_15se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 15)]
    data_16se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 16)]
    data_17se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 17)]
    data_18se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 18)]
    data_19se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 19)]
    data_20se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 20)]
    data_21se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 21)]
    data_22se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 22)]
    data_23se = df_se[(df_se['Month'] == month) & (df_se['Hour'] == 23)]

    output_se.append(data_se['DC Array Output (W)'].mean())
    output_se.append(data_1se['DC Array Output (W)'].mean())
    output_se.append(data_2se['DC Array Output (W)'].mean())
    output_se.append(data_3se['DC Array Output (W)'].mean())
    output_se.append(data_4se['DC Array Output (W)'].mean())
    output_se.append(data_5se['DC Array Output (W)'].mean())
    output_se.append(data_6se['DC Array Output (W)'].mean())
    output_se.append(data_7se['DC Array Output (W)'].mean())
    output_se.append(data_8se['DC Array Output (W)'].mean())
    output_se.append(data_9se['DC Array Output (W)'].mean())
    output_se.append(data_10se['DC Array Output (W)'].mean())
    output_se.append(data_11se['DC Array Output (W)'].mean())
    output_se.append(data_12se['DC Array Output (W)'].mean())
    output_se.append(data_13se['DC Array Output (W)'].mean())
    output_se.append(data_14se['DC Array Output (W)'].mean())
    output_se.append(data_15se['DC Array Output (W)'].mean())
    output_se.append(data_16se['DC Array Output (W)'].mean())
    output_se.append(data_17se['DC Array Output (W)'].mean())
    output_se.append(data_18se['DC Array Output (W)'].mean())
    output_se.append(data_19se['DC Array Output (W)'].mean())
    output_se.append(data_20se['DC Array Output (W)'].mean())
    output_se.append(data_21se['DC Array Output (W)'].mean())
    output_se.append(data_22se['DC Array Output (W)'].mean())
    output_se.append(data_23se['DC Array Output (W)'].mean())
    #Graph Variables
    x = hours
    y = output
    y_w = output_w
    y_m = output_m
    y_s = output_s
    y_se = output_se
    #Does the User Input Calculations
    fig, ax = plt.subplots()
    if box == 'Brookhaven' and box2 == 'Cheyenne':
        ax.plot(x,y, label = 'Brookhaven ')
        ax.plot(x, y_w, label ='Cheyenne')
    elif box == 'Brookhaven' and box2 == 'Miami':
        ax.plot(x,y, label = 'Brookhaven ')
        ax.plot(x, y_m, label = 'Miami')
    elif box == 'Brookhaven' and box2 == 'San Diego':
        ax.plot(x,y, label = 'Brookhaven ')
        ax.plot(x, y_s, label = 'San Diego')
    elif box == 'Brookhaven' and box2 == 'Seattle':
        ax.plot(x,y, label = 'Brookhaven ')
        ax.plot(x, y_se, label = 'Seattle')
    elif box == 'Cheyenne' and box2 == 'Brookhaven':
        ax.plot(x, y_w, label ='Cheyenne')
        ax.plot(x,y, label = 'Brookhaven ')
    elif box == 'Cheyenne' and box2 == 'Miami':
        ax.plot(x, y_w, label ='Cheyenne')
        ax.plot(x, y_m, label = 'Miami')
    elif box == 'Cheyenne' and box2 == 'San Diego':
        ax.plot(x, y_w, label ='Cheyenne')
        ax.plot(x, y_s, label = 'San Diego')
    elif box == 'Cheyenne' and box2 == 'Seattle':
        ax.plot(x, y_w, label ='Cheyenne')
        ax.plot(x, y_se, label = 'Seattle')
    elif box == 'Miami' and box2 == 'Brookhaven':
        ax.plot(x, y_m, label = 'Miami')
        ax.plot(x,y, label = 'Brookhaven ')
    elif box == 'Miami' and box2 == 'Cheyenne':
        ax.plot(x, y_m, label = 'Miami')
        ax.plot(x, y_w, label ='Cheyenne')
    elif box == 'Miami' and box2 == 'San Diego':
        ax.plot(x, y_m, label = 'Miami')
        ax.plot(x, y_s, label ='San Diego')
    elif box == 'Miami' and box2 == 'Seattle':
        ax.plot(x, y_m, label = 'Miami')
        ax.plot(x, y_se, label ='Seattle')
    elif box == 'San Diego' and box2 == 'Brookhaven':
        ax.plot(x, y_s, label = 'San Diego')
        ax.plot(x,y, label = 'Brookhaven ')
    elif box == 'San Diego' and box2 == 'Cheyenne':
        ax.plot(x, y_s, label = 'San Diego')
        ax.plot(x, y_w, label ='Cheyenne')
    elif box == 'San Diego' and box2 == 'Miami':
        ax.plot(x, y_s, label = 'San Diego')
        ax.plot(x, y_m, label ='Miami')
    elif box == 'San Diego' and box2 == 'Seattle':
        ax.plot(x, y_s, label = 'San Diego')
        ax.plot(x, y_se, label ='Seattle')
    elif box == 'Seattle' and box2 == 'Brookhaven':
        ax.plot(x, y_se, label = 'Seattle')
        ax.plot(x,y, label = 'Brookhaven ')
    elif box == 'Seattle' and box2 == 'Cheyenne':
        ax.plot(x, y_se, label = 'Seattle')
        ax.plot(x, y_w, label ='Cheyenne')
    elif box == 'Seattle' and box2 == 'Miami':
        ax.plot(x, y_se, label = 'Seattle')
        ax.plot(x, y_m, label ='Miami')
    elif box == 'Seattle' and box2 == 'San Diego':
        ax.plot(x, y_se, label = 'Seattle')
        ax.plot(x, y_s, label ='San Diego')
    
    plt.legend(loc = 'upper left')
    plt.xlabel("Hours")
    plt.xticks(np.arange(0, 24, 1))
    plt.ylabel('DC Array Output (W)')
   
    st.pyplot(fig)
def cumul_month():
    days = []
    #Each months has unique x List
    if month == 1:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 2:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    if month == 3:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 4:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if month == 5:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 6:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if month == 7:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 8:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 9:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if month == 10:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    if month == 11:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    if month == 12:
        days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    
    output = []
    output_w = []
    output_m = []
    output_s = []
    output_se = []

   
    data_1 = df[(df['Month'] == month) & (df['Day'] == 1)]
    data_2 = df[(df['Month'] == month) & (df['Day'] == 2)]
    data_3 = df[(df['Month'] == month) & (df['Day'] == 3)]
    data_4 = df[(df['Month'] == month) & (df['Day'] == 4)]
    data_5 = df[(df['Month'] == month) & (df['Day'] == 5)]
    data_6 = df[(df['Month'] == month) & (df['Day'] == 6)]
    data_7 = df[(df['Month'] == month) & (df['Day'] == 7)]
    data_8 = df[(df['Month'] == month) & (df['Day'] == 8)]
    data_9 = df[(df['Month'] == month) & (df['Day'] == 9)]
    data_10 = df[(df['Month'] == month) & (df['Day'] == 10)]
    data_11 = df[(df['Month'] == month) & (df['Day'] == 11)]
    data_12 = df[(df['Month'] == month) & (df['Day'] == 12)]
    data_13 = df[(df['Month'] == month) & (df['Day'] == 13)]
    data_14 = df[(df['Month'] == month) & (df['Day'] == 14)]
    data_15 = df[(df['Month'] == month) & (df['Day'] == 15)]
    data_16 = df[(df['Month'] == month) & (df['Day'] == 16)]
    data_17 = df[(df['Month'] == month) & (df['Day'] == 17)]
    data_18 = df[(df['Month'] == month) & (df['Day'] == 18)]
    data_19 = df[(df['Month'] == month) & (df['Day'] == 19)]
    data_20 = df[(df['Month'] == month) & (df['Day'] == 20)]
    data_21 = df[(df['Month'] == month) & (df['Day'] == 21)]
    data_22 = df[(df['Month'] == month) & (df['Day'] == 22)]
    data_23 = df[(df['Month'] == month) & (df['Day'] == 23)]
    data_24 = df[(df['Month'] == month) & (df['Day'] == 24)]
    data_25 = df[(df['Month'] == month) & (df['Day'] == 25)]
    data_26 = df[(df['Month'] == month) & (df['Day'] == 26)]
    data_27 = df[(df['Month'] == month) & (df['Day'] == 27)]
    data_28 = df[(df['Month'] == month) & (df['Day'] == 28)]
    data_29 = df[(df['Month'] == month) & (df['Day'] == 29)]
    data_30 = df[(df['Month'] == month) & (df['Day'] == 30)]
    data_31 = df[(df['Month'] == month) & (df['Day'] == 31)]

    output.append(sum(data_1['DC Array Output (W)']))
    output.append(sum(data_2['DC Array Output (W)']))
    output.append(sum(data_3['DC Array Output (W)']))
    output.append(sum(data_4['DC Array Output (W)']))
    output.append(sum(data_5['DC Array Output (W)']))
    output.append(sum(data_6['DC Array Output (W)']))
    output.append(sum(data_7['DC Array Output (W)']))
    output.append(sum(data_8['DC Array Output (W)']))
    output.append(sum(data_9['DC Array Output (W)']))
    output.append(sum(data_10['DC Array Output (W)']))
    output.append(sum(data_11['DC Array Output (W)']))
    output.append(sum(data_12['DC Array Output (W)']))
    output.append(sum(data_13['DC Array Output (W)']))
    output.append(sum(data_14['DC Array Output (W)']))
    output.append(sum(data_15['DC Array Output (W)']))
    output.append(sum(data_16['DC Array Output (W)']))
    output.append(sum(data_17['DC Array Output (W)']))
    output.append(sum(data_18['DC Array Output (W)']))
    output.append(sum(data_19['DC Array Output (W)']))
    output.append(sum(data_20['DC Array Output (W)']))
    output.append(sum(data_21['DC Array Output (W)']))
    output.append(sum(data_22['DC Array Output (W)']))
    output.append(sum(data_23['DC Array Output (W)']))
    output.append(sum(data_24['DC Array Output (W)']))
    output.append(sum(data_25['DC Array Output (W)']))
    output.append(sum(data_26['DC Array Output (W)']))
    output.append(sum(data_27['DC Array Output (W)']))
    output.append(sum(data_28['DC Array Output (W)']))
    output.append(sum(data_29['DC Array Output (W)']))
    output.append(sum(data_30['DC Array Output (W)']))
    output.append(sum(data_31['DC Array Output (W)']))
    #Cheyenne
    data_1w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 1)]
    data_2w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 2)]
    data_3w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 3)]
    data_4w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 4)]
    data_5w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 5)]
    data_6w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 6)]
    data_7w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 7)]
    data_8w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 8)]
    data_9w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 9)]
    data_10w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 10)]
    data_11w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 11)]
    data_12w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 12)]
    data_13w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 13)]
    data_14w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 14)]
    data_15w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 15)]
    data_16w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 16)]
    data_17w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 17)]
    data_18w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 18)]
    data_19w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 19)]
    data_20w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 20)]
    data_21w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 21)]
    data_22w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 22)]
    data_23w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 23)]
    data_24w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 24)]
    data_25w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 25)]
    data_26w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 26)]
    data_27w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 27)]
    data_28w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 28)]
    data_29w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 29)]
    data_30w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 30)]
    data_31w = df_w[(df_w['Month'] == month) & (df_w['Day'] == 31)]

    output_w.append(sum(data_1w['DC Array Output (W)']))
    output_w.append(sum(data_2w['DC Array Output (W)']))
    output_w.append(sum(data_3w['DC Array Output (W)']))
    output_w.append(sum(data_4w['DC Array Output (W)']))
    output_w.append(sum(data_5w['DC Array Output (W)']))
    output_w.append(sum(data_6w['DC Array Output (W)']))
    output_w.append(sum(data_7w['DC Array Output (W)']))
    output_w.append(sum(data_8w['DC Array Output (W)']))
    output_w.append(sum(data_9w['DC Array Output (W)']))
    output_w.append(sum(data_10w['DC Array Output (W)']))
    output_w.append(sum(data_11w['DC Array Output (W)']))
    output_w.append(sum(data_12w['DC Array Output (W)']))
    output_w.append(sum(data_13w['DC Array Output (W)']))
    output_w.append(sum(data_14w['DC Array Output (W)']))
    output_w.append(sum(data_15w['DC Array Output (W)']))
    output_w.append(sum(data_16w['DC Array Output (W)']))
    output_w.append(sum(data_17w['DC Array Output (W)']))
    output_w.append(sum(data_18w['DC Array Output (W)']))
    output_w.append(sum(data_19w['DC Array Output (W)']))
    output_w.append(sum(data_20w['DC Array Output (W)']))
    output_w.append(sum(data_21w['DC Array Output (W)']))
    output_w.append(sum(data_22w['DC Array Output (W)']))
    output_w.append(sum(data_23w['DC Array Output (W)']))
    output_w.append(sum(data_24w['DC Array Output (W)']))
    output_w.append(sum(data_25w['DC Array Output (W)']))
    output_w.append(sum(data_26w['DC Array Output (W)']))
    output_w.append(sum(data_27w['DC Array Output (W)']))
    output_w.append(sum(data_28w['DC Array Output (W)']))
    output_w.append(sum(data_29w['DC Array Output (W)']))
    output_w.append(sum(data_30w['DC Array Output (W)']))
    output_w.append(sum(data_31w['DC Array Output (W)']))
    #Miami
    data_1m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 1)]
    data_2m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 2)]
    data_3m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 3)]
    data_4m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 4)]
    data_5m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 5)]
    data_6m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 6)]
    data_7m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 7)]
    data_8m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 8)]
    data_9m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 9)]
    data_10m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 10)]
    data_11m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 11)]
    data_12m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 12)]
    data_13m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 13)]
    data_14m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 14)]
    data_15m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 15)]
    data_16m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 16)]
    data_17m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 17)]
    data_18m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 18)]
    data_19m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 19)]
    data_20m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 20)]
    data_21m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 21)]
    data_22m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 22)]
    data_23m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 23)]
    data_24m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 24)]
    data_25m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 25)]
    data_26m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 26)]
    data_27m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 27)]
    data_28m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 28)]
    data_29m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 29)]
    data_30m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 30)]
    data_31m = df_m[(df_m['Month'] == month) & (df_m['Day'] == 31)]

    output_m.append(sum(data_1m['DC Array Output (W)']))
    output_m.append(sum(data_2m['DC Array Output (W)']))
    output_m.append(sum(data_3m['DC Array Output (W)']))
    output_m.append(sum(data_4m['DC Array Output (W)']))
    output_m.append(sum(data_5m['DC Array Output (W)']))
    output_m.append(sum(data_6m['DC Array Output (W)']))
    output_m.append(sum(data_7m['DC Array Output (W)']))
    output_m.append(sum(data_8m['DC Array Output (W)']))
    output_m.append(sum(data_9m['DC Array Output (W)']))
    output_m.append(sum(data_10m['DC Array Output (W)']))
    output_m.append(sum(data_11m['DC Array Output (W)']))
    output_m.append(sum(data_12m['DC Array Output (W)']))
    output_m.append(sum(data_13m['DC Array Output (W)']))
    output_m.append(sum(data_14m['DC Array Output (W)']))
    output_m.append(sum(data_15m['DC Array Output (W)']))
    output_m.append(sum(data_16m['DC Array Output (W)']))
    output_m.append(sum(data_17m['DC Array Output (W)']))
    output_m.append(sum(data_18m['DC Array Output (W)']))
    output_m.append(sum(data_19m['DC Array Output (W)']))
    output_m.append(sum(data_20m['DC Array Output (W)']))
    output_m.append(sum(data_21m['DC Array Output (W)']))
    output_m.append(sum(data_22m['DC Array Output (W)']))
    output_m.append(sum(data_23m['DC Array Output (W)']))
    output_m.append(sum(data_24m['DC Array Output (W)']))
    output_m.append(sum(data_25m['DC Array Output (W)']))
    output_m.append(sum(data_26m['DC Array Output (W)']))
    output_m.append(sum(data_27m['DC Array Output (W)']))
    output_m.append(sum(data_28m['DC Array Output (W)']))
    output_m.append(sum(data_29m['DC Array Output (W)']))
    output_m.append(sum(data_30m['DC Array Output (W)']))
    output_m.append(sum(data_31m['DC Array Output (W)']))
    #San Diego
    data_1s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 1)]
    data_2s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 2)]
    data_3s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 3)]
    data_4s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 4)]
    data_5s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 5)]
    data_6s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 6)]
    data_7s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 7)]
    data_8s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 8)]
    data_9s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 9)]
    data_10s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 10)]
    data_11s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 11)]
    data_12s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 12)]
    data_13s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 13)]
    data_14s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 14)]
    data_15s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 15)]
    data_16s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 16)]
    data_17s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 17)]
    data_18s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 18)]
    data_19s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 19)]
    data_20s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 20)]
    data_21s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 21)]
    data_22s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 22)]
    data_23s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 23)]
    data_24s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 24)]
    data_25s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 25)]
    data_26s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 26)]
    data_27s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 27)]
    data_28s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 28)]
    data_29s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 29)]
    data_30s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 30)]
    data_31s = df_s[(df_s['Month'] == month) & (df_s['Day'] == 31)]

    output_s.append(sum(data_1s['DC Array Output (W)']))
    output_s.append(sum(data_2s['DC Array Output (W)']))
    output_s.append(sum(data_3s['DC Array Output (W)']))
    output_s.append(sum(data_4s['DC Array Output (W)']))
    output_s.append(sum(data_5s['DC Array Output (W)']))
    output_s.append(sum(data_6s['DC Array Output (W)']))
    output_s.append(sum(data_7s['DC Array Output (W)']))
    output_s.append(sum(data_8s['DC Array Output (W)']))
    output_s.append(sum(data_9s['DC Array Output (W)']))
    output_s.append(sum(data_10s['DC Array Output (W)']))
    output_s.append(sum(data_11s['DC Array Output (W)']))
    output_s.append(sum(data_12s['DC Array Output (W)']))
    output_s.append(sum(data_13s['DC Array Output (W)']))
    output_s.append(sum(data_14s['DC Array Output (W)']))
    output_s.append(sum(data_15s['DC Array Output (W)']))
    output_s.append(sum(data_16s['DC Array Output (W)']))
    output_s.append(sum(data_17s['DC Array Output (W)']))
    output_s.append(sum(data_18s['DC Array Output (W)']))
    output_s.append(sum(data_19s['DC Array Output (W)']))
    output_s.append(sum(data_20s['DC Array Output (W)']))
    output_s.append(sum(data_21s['DC Array Output (W)']))
    output_s.append(sum(data_22s['DC Array Output (W)']))
    output_s.append(sum(data_23s['DC Array Output (W)']))
    output_s.append(sum(data_24s['DC Array Output (W)']))
    output_s.append(sum(data_25s['DC Array Output (W)']))
    output_s.append(sum(data_26s['DC Array Output (W)']))
    output_s.append(sum(data_27s['DC Array Output (W)']))
    output_s.append(sum(data_28s['DC Array Output (W)']))
    output_s.append(sum(data_29s['DC Array Output (W)']))
    output_s.append(sum(data_30s['DC Array Output (W)']))
    output_s.append(sum(data_31s['DC Array Output (W)']))
    #Seattle
    data_1se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 1)]
    data_2se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 2)]
    data_3se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 3)]
    data_4se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 4)]
    data_5se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 5)]
    data_6se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 6)]
    data_7se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 7)]
    data_8se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 8)]
    data_9se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 9)]
    data_10se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 10)]
    data_11se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 11)]
    data_12se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 12)]
    data_13se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 13)]
    data_14se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 14)]
    data_15se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 15)]
    data_16se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 16)]
    data_17se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 17)]
    data_18se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 18)]
    data_19se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 19)]
    data_20se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 20)]
    data_21se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 21)]
    data_22se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 22)]
    data_23se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 23)]
    data_24se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 24)]
    data_25se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 25)]
    data_26se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 26)]
    data_27se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 27)]
    data_28se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 28)]
    data_29se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 29)]
    data_30se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 30)]
    data_31se = df_se[(df_se['Month'] == month) & (df_se['Day'] == 31)]

    output_se.append(sum(data_1se['DC Array Output (W)']))
    output_se.append(sum(data_2se['DC Array Output (W)']))
    output_se.append(sum(data_3se['DC Array Output (W)']))
    output_se.append(sum(data_4se['DC Array Output (W)']))
    output_se.append(sum(data_5se['DC Array Output (W)']))
    output_se.append(sum(data_6se['DC Array Output (W)']))
    output_se.append(sum(data_7se['DC Array Output (W)']))
    output_se.append(sum(data_8se['DC Array Output (W)']))
    output_se.append(sum(data_9se['DC Array Output (W)']))
    output_se.append(sum(data_10se['DC Array Output (W)']))
    output_se.append(sum(data_11se['DC Array Output (W)']))
    output_se.append(sum(data_12se['DC Array Output (W)']))
    output_se.append(sum(data_13se['DC Array Output (W)']))
    output_se.append(sum(data_14se['DC Array Output (W)']))
    output_se.append(sum(data_15se['DC Array Output (W)']))
    output_se.append(sum(data_16se['DC Array Output (W)']))
    output_se.append(sum(data_17se['DC Array Output (W)']))
    output_se.append(sum(data_18se['DC Array Output (W)']))
    output_se.append(sum(data_19se['DC Array Output (W)']))
    output_se.append(sum(data_20se['DC Array Output (W)']))
    output_se.append(sum(data_21se['DC Array Output (W)']))
    output_se.append(sum(data_22se['DC Array Output (W)']))
    output_se.append(sum(data_23se['DC Array Output (W)']))
    output_se.append(sum(data_24se['DC Array Output (W)']))
    output_se.append(sum(data_25se['DC Array Output (W)']))
    output_se.append(sum(data_26se['DC Array Output (W)']))
    output_se.append(sum(data_27se['DC Array Output (W)']))
    output_se.append(sum(data_28se['DC Array Output (W)']))
    output_se.append(sum(data_29se['DC Array Output (W)']))
    output_se.append(sum(data_30se['DC Array Output (W)']))
    output_se.append(sum(data_31se['DC Array Output (W)']))
    #The whiles just removes the empty days in the function
    while (output.count(0)):
        output.remove(0)
    while (output_w.count(0)):
        output_w.remove(0)
    while (output_m.count(0)):
        output_m.remove(0)
    while (output_s.count(0)):
        output_s.remove(0)
    while (output_se.count(0)):
        output_se.remove(0)
    #Variables
    fig, ax = plt.subplots()
    x = days
    y = output
    y_w = output_w
    y_m = output_m
    y_s = output_s
    y_se = output_se
    #User Input Format
    if box == 'Brookhaven' and box2 == 'Cheyenne':
        ax.bar(x,y, label = 'Brookhaven ', color = 'Red', alpha = 0.5)
        ax.bar(x, y_w, label ='Cheyenne', color = 'Blue', alpha = 0.5)
    elif box == 'Brookhaven' and box2 == 'Miami':
        ax.bar(x,y, label = 'Brookhaven ', color = 'Red', alpha = 0.5)
        ax.bar(x, y_m, label = 'Miami', color = 'Blue', alpha = 0.5)
    elif box == 'Brookhaven' and box2 == 'San Diego':
        ax.bar(x,y, label = 'Brookhaven ', color = 'Red', alpha = 0.5)
        ax.bar(x, y_s, label = 'San Diego', color = 'Blue', alpha = 0.5)
    elif box == 'Brookhaven' and box2 == 'Seattle':
        ax.bar(x,y, label = 'Brookhaven ', color = 'Red', alpha = 0.5)
        ax.bar(x, y_se, label = 'Seattle', color = 'Blue', alpha = 0.5)
    elif box == 'Cheyenne' and box2 == 'Brookhaven':
        ax.bar(x, y_w, label ='Cheyenne', color = 'Red', alpha = 0.5)
        ax.bar(x,y, label = 'Brookhaven ', color = 'Blue', alpha = 0.5)
    elif box == 'Cheyenne' and box2 == 'Miami':
        ax.bar(x, y_w, label ='Cheyenne', color = 'Red', alpha = 0.5)
        ax.bar(x, y_m, label = 'Miami', color = 'Blue', alpha = 0.5)
    elif box == 'Cheyenne' and box2 == 'San Diego':
        ax.bar(x, y_w, label ='Cheyenne', color = 'Red', alpha = 0.5)
        ax.bar(x, y_s, label = 'San Diego', color = 'Blue', alpha = 0.5)
    elif box == 'Cheyenne' and box2 == 'Seattle':
        ax.bar(x, y_w, label ='Cheyenne', color = 'Red', alpha = 0.5)
        ax.bar(x, y_se, label = 'Seattle', color = 'Blue', alpha = 0.5)
    elif box == 'Miami' and box2 == 'Brookhaven':
        ax.bar(x, y_m, label = 'Miami', color = 'Red', alpha = 0.5)
        ax.bar(x,y, label = 'Brookhaven ', color = 'Blue', alpha = 0.5)
    elif box == 'Miami' and box2 == 'Cheyenne':
        ax.bar(x, y_m, label = 'Miami', color = 'Red', alpha = 0.5)
        ax.bar(x, y_w, label ='Cheyenne', color = 'Blue', alpha = 0.5)
    elif box == 'Miami' and box2 == 'San Diego':
        ax.bar(x, y_m, label = 'Miami', color = 'Red', alpha = 0.5)
        ax.bar(x, y_s, label ='San Diego', color = 'Blue', alpha = 0.5)
    elif box == 'Miami' and box2 == 'Seattle':
        ax.bar(x, y_m, label = 'Miami', color = 'Red', alpha = 0.5)
        ax.bar(x, y_se, label ='Seattle', color = 'Blue', alpha = 0.5)
    elif box == 'San Diego' and box2 == 'Brookhaven':
        ax.bar(x, y_s, label = 'San Diego', color = 'Red', alpha = 0.5)
        ax.bar(x,y, label = 'Brookhaven ', color = 'Blue', alpha = 0.5)
    elif box == 'San Diego' and box2 == 'Cheyenne':
        ax.bar(x, y_s, label = 'San Diego', color = 'Red', alpha = 0.5)
        ax.bar(x, y_w, label ='Cheyenne', color = 'Blue', alpha = 0.5)
    elif box == 'San Diego' and box2 == 'Miami':
        ax.bar(x, y_s, label = 'San Diego', color = 'Red', alpha = 0.5)
        ax.bar(x, y_m, label ='Miami', color = 'Blue', alpha = 0.5)
    elif box == 'San Diego' and box2 == 'Seattle':
        ax.bar(x, y_s, label = 'San Diego', color = 'Red', alpha = 0.5)
        ax.bar(x, y_se, label ='Seattle', color = 'Blue', alpha = 0.5)
    elif box == 'Seattle' and box2 == 'Brookhaven':
        ax.bar(x, y_se, label = 'Seattle', color = 'Red', alpha = 0.5)
        ax.bar(x,y, label = 'Brookhaven ', color = 'Blue', alpha = 0.5)
    elif box == 'Seattle' and box2 == 'Cheyenne':
        ax.bar(x, y_se, label = 'Seattle', color = 'Red', alpha = 0.5)
        ax.bar(x, y_w, label ='Cheyenne', color = 'Blue', alpha = 0.5)
    elif box == 'Seattle' and box2 == 'Miami':
        ax.bar(x, y_se, label = 'Seattle', color = 'Red', alpha = 0.5)
        ax.bar(x, y_m, label ='Miami', color = 'Blue', alpha = 0.5)
    elif box == 'Seattle' and box2 == 'San Diego':
        ax.bar(x, y_se, label = 'Seattle', color = 'Red', alpha = 0.5)
        ax.bar(x, y_s, label ='San Diego', color = 'Blue', alpha = 0.5)

    plt.legend(loc = 'upper left')
    plt.xlabel("Days")
    plt.xticks(np.arange(1, int(len(days)), 4))
    plt.ylabel('DC Array Output (W)')
    st.pyplot(fig)
def map():
    county_population = pd.read_csv('cities.csv')
# view (location, zoom level, etc.)

    chart = pdk.Deck(
        map_style="dark",
        initial_view_state={
            "country": "usa",
            "latitude":39.155726,
            "longitude": -98.030561 ,
            "zoom": 3,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HeatmapLayer",
                data=county_population,
                get_position=['Longitude', 'Latitude'],
                auto_highlight=True,
                pickable=True,
                color_range=BrwnYl_3.colors,
                get_weight = ['PVWatts'],
                threshold=0.2,
                radius=5000,
            ),
        ],
    )
        
    st.pydeck_chart(chart)

#More GUI Formatting
with st.expander('Hourly Average DC Array Output (W)'):
    dc_array_output()
with st.expander('Cumulative Daily DC Array Output(W)'):
    cumul_month()
with st.expander('Annual DC Array Outpu(W) Heatmap'):
    map()



