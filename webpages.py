import streamlit as st
import pipeline as pp
import display as dis
import eda
import pandas as pd
from streamlit_lottie import st_lottie
import animations as anima

proj_desc_1 =  '''
    <p style="font-size:20px">
    Hey Guys!!!🙋‍♂️ Welcome to my Webapp 🙌🎆. 
    This website is used to predict the selling price💲of used cars 🚗 based on 5 specific features of the car.<br> 
    This website estimates the selling price💲 of any car🚙 based on Machine Learning Approach. In the Machine Learning approach, we provide the Machine
    learning algorithm with some data. Then the algorithm creates a Machine Learning model which estimates the selling price of used cars
    based on 5 specific features of the car. The input to the machine learning model would be given by the end user or the 
    client. <br> 
    The data is collected from kaggle, which was collected by a kaggle user from \'Car Dekho.com\' . <br> 
    </p>
    '''

proj_desc_2 = '''
    <p style="font-size:20px">
    \'CarDekho.com\' is India's leading car search venture that helps users buy cars that are right for them. It's website and app carry rich automotive
    content such as expert reviews, detailed specs & prices, comparisions as well as videos & pictures of all car brands & models available in india. <br> 
    </p>
'''

eda_text_1 = '''
    <p style="font-size:20px">
    This page shows Exploratory Data Analysis(EDA) of my project. Exploratory Data Analysis(EDA) is the process of investigating the dataset to discover patterns, 
    and anomalies (outliers), and form hypotheses based on our understanding of the dataset. <br>
    The checkbox below is used to view my project data.
    </p>
'''

eda_text_2 = '''
    <p style="font-size:20px">
    <br>The following is the statistical information about my project data. 
    </p>
'''

eda_text_3 = '''
    <p style="font-size:20px">
    <br>The following are the features of my project data.
    </p>
'''

eda_text_4 = '''
    <p font-size:30px;>
    <ul style="background-color:powderblue;color:black;">
        <li> car_name - Name of the car </li>
        <li> brand - Brand of the car </li>
        <li> model - Car model </li>
        <li>min_cost_price - Minimum cost price of the car</li>     
        <li> max_cost_price - Maximum cost price of the car</li>       
        <li> vehicle_age - age of the vehicle </li>       
        <li> km_driven - distance travelled with your vehicle </li>      
        <li> seller_type - Individual or a Dealer </li>    
        <li> fuel_type - CNG, Petrol, Diesel or Eletric </li>     
        <li> transmission_type - Manual or Automatic </li>     
        <li> mileage - The distance that has been travelled, measured in miles </li>   
        <li> engine - The part of a vehicle that produces power to make the vehicle move </li>
        <li> max_power - The maximum power that an engine can produce </li>
        <li> seats - Number of passenger seats </li>
        <li> selling_price - The price at which the car is sold </li>
        
    </ul>
    </p>
'''

eda_text_5 = '''
    <p style="font-size:20px">
    <br>Correlation is used to describe the linear relationship between two continuous variables. It measures the strength (qualitatively) 
    and direction of the linear relationship between two or more variables.
    </p>
'''

eda_text_6 = '''
    <p style="font-size:20px">
    <br>Popularity of the car based on fuel type.
    </p>
'''

eda_text_7 = '''
    <p style="font-size:20px">
    <br>The following graph is used to visualize the relation between ENGINE and MILEAGE features.
    </p>
'''


home_page_gif = r'home_page.json'

eda_page_gif = r'analysis_3.json'

predict_page_gif = r'price_1.json'

eda_title = '<p style="serif;color:#2cd361;font-size:40px;"><center> Exploratory Data Analysis </center></p>'

predict_header = '<p style="serif;color:#FCE205;font-size:40px;"><center> Predict Selling Price Of Your Car </center></p>'

website_title = '<p style="font-family:Franklin Gothic Medium;color:#FF5700;font-size:45px;"><center>PRICE PREDICTION OF USED CARS USING MACHINE LEARNING</center></p>'

file_path = r'Data\MAIN DATA.csv'

gif_1 = anima.loadLottie(home_page_gif)

gif_2 = anima.loadLottie(eda_page_gif)

gif_3 = anima.loadLottie(predict_page_gif)

## USER-DEFINED FUNCTIONS  
   
def homePage() :
        
    ''' FUNCTION TO CREATE HOME PAGE'''
    
    # WEB-PAGE TITLE
    st.markdown(website_title,unsafe_allow_html=True)
    
    # DISPLAY ANIMATION    
    st_lottie(gif_1,speed=0.8,reverse=False,loop=True,quality='high',height=500)
    
    # DISPLAYING TEXT
    st.markdown(proj_desc_1,unsafe_allow_html=True)
    
    # DISPLAYING TEXT
    st.markdown(proj_desc_2,unsafe_allow_html=True)
    
    
    
       
def edaPage() :
        
    ''' FUNCTION TO CREATE EDA PAGE'''    
        
    # DISPLAYING TEXT
    st.markdown(eda_title,unsafe_allow_html=True)
    
    # DISPLAY ANIMATION    
    st_lottie(gif_2,speed=0.7,reverse=False,loop=False,quality='high',height=550)
    
    # DISPLAY TEXT
    st.markdown(eda_text_1,unsafe_allow_html=True)
    
    # IF CHECKBOX IS CLICKED   
    if st.checkbox('View Data'.upper() , key = 1) :
        
        # SHOW DATA
        data = eda.showData()
        
         # DISPLAY DATAFRAME
        st.dataframe(data)
        
    # DISPLAY TEXT
    st.markdown(eda_text_2,unsafe_allow_html=True)    
        
    # IF CHECKBOX IS CLICKED   
    if st.checkbox('View Information about the data'.upper() , key = 2) :
        
        # SHOW DATA
        data = eda.dataInfo()
        
         # DISPLAY DATAFRAME
        st.write(data)    
    
    # DISPLAY TEXT
    st.markdown(eda_text_3,unsafe_allow_html=True)    
        
    if st.checkbox('view features'.upper() , key = 3) :
        
        # DISPLAY TEXT
        st.markdown(eda_text_4,unsafe_allow_html=True)    
        
    # DISPLAY TEXT
    st.markdown(eda_text_5,unsafe_allow_html=True)    
        
    if st.checkbox('view cor-relation'.upper() ,  key = 4) :
        
        # DISPLAY TEXT
        cor_plot = eda.corrPlot()        
        
        st.header('Cor-relation Matrix'.upper())
        
        st.plotly_chart(cor_plot)     
        
    # DISPLAY TEXT
    st.markdown(eda_text_6,unsafe_allow_html=True)
    
    if  st.checkbox('view graph'.upper() , key = 5):
        
        # DISPLAY TEXT
        pie_plot = eda.plot2()   
        
        st.header('Car market based on fuel type'.upper())
        
        st.plotly_chart(pie_plot)  
           
     
    # DISPLAY TEXT
    st.markdown(eda_text_7,unsafe_allow_html=True)
    
    if  st.checkbox('view graph'.upper() , key = 6):
        
        # DISPLAY TEXT
        scatter_plot = eda.plot3()   
        
        st.header('ENGINE (VS) MILEAGE'.upper())
        
        st.plotly_chart(scatter_plot)  
        

def predictPage() :
    
    ''' FUNCTION TO CREATE PRICE PREDICTION PAGE'''
    
    # PAGE HEADER
    st.markdown(predict_header,unsafe_allow_html=True)
    
    # DISPLAY ANIMATION    
    st_lottie(gif_3,speed=1,reverse=False,loop=True,quality='high',height=550)
    
    
    ## INPUTS FOR OUR MODEL
    inp1 = st.slider('Select the minimum cost price of your vehicle : '.title() , min_value = 50000 , max_value = 9000000 , step = 10000 , value = 50000)
    
    inp2 = st.slider('Select the maximum cost price of your vehicle : '.title() , min_value = 100000 , max_value = 10000000 , step = 10000 , value = 100000)
    
    inp3 = st.slider('Select the total distance travelled with your vehicle  : '.title() , min_value = 100 , max_value = 300000 , step = 100 , value = 100)
    
    inp4 = st.slider('Select the age of your vehicle : '.title() , min_value = 0 , max_value = 15 , value = 0)
    
    inp5 = st.slider('Select your car\'s mileage : '.title() , min_value = 4.00 , max_value = 35.00 , value = 4.00)
    
    
    # SPLITTING INTO # COLUMNS
    col1, col2, col3 = st.columns([4.5,4,2])
    
    # ALIGNING THE IMAGE IN THE CENTER
    with col1:
        
        st.write("")

    with col2:
        
       # SUBMIT BUTTON
        submit = st.button('Submit details')

    with col3:
        
        st.write("")
    
    # IF SUBMIT BUTTON IS CLICKED
    if submit :
            
            data = [inp3,inp4,inp2,inp1,inp5]
            
            new_data = pp.preProcess(data)
            
            sell_price = pp.predictPrice(new_data)
            
            dis.displayOutput(sell_price)
        
    