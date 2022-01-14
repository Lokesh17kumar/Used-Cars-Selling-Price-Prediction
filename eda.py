import pandas as pd
import streamlit as st
import cufflinks as cf
import plotly.offline

# USING CUFFLINKS IN OFFLINE MODE
cf.go_offline()

# CONFIGURING 'config' file
cf.set_config_file(offline=True, world_readable=True,sharing=True)

file_path = r'Data\MAIN DATA.csv'

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
def dataCol() :
    
    ''' Function to display columns'''
    
   