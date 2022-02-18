import pandas as pd
import streamlit as st
import cufflinks as cf
import plotly.offline
import plotly.express as px

# USING CUFFLINKS IN OFFLINE MODE
cf.go_offline()

# CONFIGURING 'config' file
cf.set_config_file(offline=True, world_readable=True,sharing=True)

file_path = r'MAIN DATA.csv'

@st.experimental_memo
def showData() :
    
    ''' Function to display data''' 
     
    with open(file_path,'rb') as file :   
        
        data = pd.read_csv(file)
   
    return data
   
@st.experimental_memo
def dataInfo() :
    
    ''' Function to display statistics about data'''
    
    data = showData()
    
    return data.describe()


@st.experimental_memo
def corrPlot() :
    
    ''' Function to display cor-relation matrix'''
    
    data = showData()
    
    data_corr = data.corr()
    
    return px.imshow(data_corr , text_auto=True , aspect = 'auto' , zmin=-1 )
    

@st.experimental_memo
def plot2() :
    
    ''' Function to display bar graph'''
    
    data = showData()
    
    fuel_type_val_count = data['fuel_type'].value_counts()
    
    new_data = {'FUEL TYPE' : fuel_type_val_count.index , 'CAR COUNT' : fuel_type_val_count.values }
    
    car_count = pd.DataFrame(new_data)
    
    return px.pie(car_count , names = car_count['FUEL TYPE'] , values = car_count['CAR COUNT'] )
    
    
    
@st.experimental_memo
def plot3() :
    
    ''' Function to display bar graph'''
    
    data = showData()

    return px.scatter(data, x="engine", y="mileage",color = 'fuel_type' , symbol = 'fuel_type' , title = 'ENGINE (VS) MILEAGE'.upper(),color_continuous_scale=["red", "green", "blue","black","purple"])
    
      