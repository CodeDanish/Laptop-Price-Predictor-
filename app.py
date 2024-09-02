import streamlit as st
import pandas as pd 
import pickle as pkl
import numpy as np 

loaded_model = pkl.load(open('regressor.pkl','rb'))
laptop_df = pkl.load(open('laptop.pkl','rb'))

st.title('Laptop Price Predictor')

# Getting the input data from user
# columns for input field
col1, col2, col3 = st.columns(3)

with col1:
    #Brand
    brand = st.selectbox('Brand', laptop_df['Company'].unique())
    brand_value = np.unique(laptop_df['Company'])
    brand_value = list(brand_value)
    brand_index = float(brand_value.index(brand))

with col2:
    #TypeName
    typename = st.selectbox('Type Name', laptop_df['TypeName'].unique())
    typename_value = np.unique(laptop_df['TypeName'])
    typename_value = list(typename_value)
    typename_index = float(typename_value.index(typename))

with col3:
    #Ram
    ram = st.selectbox('Ram (GB)', laptop_df['Ram (GB)'].unique())

with col1:
    #Weight
    weight = st.number_input('Weight')

with col2:
    #TouchScreen
    touchscreen = st.selectbox('TouchScreen', ['No','Yes'])

with col3:
    #IPS
    ips = st.selectbox('IPS', ['No','Yes'])

with col1:
    #ScreenSize
    screensize = st.number_input('Screen Size')

with col2:
    #Resolution
    resolution = st.selectbox('Screen Resolution',['1920x1000','1366x768','1600x900','3840x2160','3200x1800','2880x1800'
                                                    ,'2560x1600','2560x1600','2304x1440'])
with col3:
    #CPU
    cpu = st.selectbox('CPU',laptop_df['Cpu Brand'].unique())
    cpu_value = np.unique(laptop_df['Cpu Brand'])
    cpu_value = list(cpu_value)
    cpu_index = float(cpu_value.index(cpu))
    
with col1:
    #HDD
    hdd = st.selectbox('HDD (GB)',[0,128,256,512,1024,2048])

with col2:
    #SSD
    ssd = st.selectbox('SSD (GB)',[0,8,128,256,512,1024])

with col3:
    #GPU
    gpu = st.selectbox('GPU',laptop_df['Gpu Brand'].unique())
    gpu_value = np.unique(laptop_df['Gpu Brand'])
    gpu_value = list(gpu_value)
    gpu_index = float(gpu_value.index(gpu))

with col1:
    #OS
    os = st.selectbox('OS',laptop_df['OpSys'].unique())
    os_value = np.unique(laptop_df['OpSys'])
    os_value = list(os_value)
    os_index = float(os_value.index(os))

if st.button('Predict Price'):

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])

    ppi = (x_res**2 + y_res**2)**0.5/screensize

    #Query
    query = np.array([brand_index,typename_index,screensize,ram,gpu_index,os_index,
                                        weight,ips,touchscreen,ppi,cpu_index,ssd,hdd])

    query_value = query.reshape(1,13)

    prediction = loaded_model.predict(query_value)

    st.title("The predicted price for the above configuraton is "+ str(np.exp(prediction[0])))







