import streamlit as st
import pipeline as pp
import display as dis
import eda
import pandas as pd

proj_desc_1 =  '''
    <p style="font-size:20px">
    Hey Guys!!!🙋‍♂️ Welcome to my Webapp 🙌🎆. <br> 
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
    Correlation is an indication about the changes between two variables. The checkbox below is used to view cor-relation between my data. 
    </p>
'''

eda_text_3 = '''
    <p style="font-size:20px">
    The following are the features of my project data.
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



sell_image = r'Images\predict_page_img3.jpg'

marketing_image = r'Images\Akshay-Kumar-CarDekho.png'        

eda_logo = r'Images\eda.jpg'

eda_title = '<p style="serif;color:#2cd361;font-size:40px;"><center> Exploratory Data Analysis </center></p>'

predict_header = '<p style="serif;color:#FCE205;font-size:40px;"><center> Predict Selling Price💲of your car🚗 </center></p>'

website_title = '<p style="font-family:Franklin Gothic Medium;color:#FF5700;font-size:40px;"><center>PRICE💲 PREDICTION OF USED CARS🚗🏎️🚙 USING MACHINE LEARNING</center></p>'

file_path = r'Data\MAIN DATA.csv'


## USER-DEFINED FUNCTIONS  

def buttonAlignCenter(text):
    
    ''' Function to align button in the center'''
    
    # SPLITTING INTO # COLUMNS
    col1, col2, col3 = st.columns([2, 5, 2])
    
    # ALIGNING THE IMAGE IN THE CENTER
    with col1:
        
        st.write("")

    with col2:
        
        pass
        # DISPLAYING IMAGE IN THE CENTER
        #col2.

    with col3:
        
        st.write("")


def imageAlignCenter(img):
    
    ''' Function to align Image in the center'''
    
    # SPLITTING INTO # COLUMNS
    col1, col2, col3 = st.columns([2, 5, 2])
    
    # ALIGNING THE IMAGE IN THE CENTER
    with col1:
        
        st.write("")

    with col2:
        
        # DISPLAYING IMAGE IN THE CENTER
        col2.image(img,use_column_width=True)

    with col3:
        
        st.write("")



   
def homePage() :
        
    ''' FUNCTION TO CREATE HOME PAGE'''
    
    # WEB-PAGE TITLE
    st.markdown(website_title,unsafe_allow_html=True)
    
    # DISPLAY IMAGE
    imageAlignCenter(marketing_image)
    
    # DISPLAYING TEXT
    st.markdown(proj_desc_1,unsafe_allow_html=True)
    
    # DISPLAYING TEXT
    st.markdown(proj_desc_2,unsafe_allow_html=True)
    
    
    
       
def edaPage() :
        
    ''' FUNCTION TO CREATE EDA PAGE'''    
        
    # DISPLAYING TEXT
    st.markdown(eda_title,unsafe_allow_html=True)
    
    # SPLITTING INTO # COLUMNS
    col1, col2, col3 = st.columns([2, 5, 2])
    
    # DISPLAY IMAGE
    imageAlignCenter(eda_logo)
    
    # DISPLAY TEXT
    st.markdown(eda_text_1,unsafe_allow_html=True)
    
    # IF CHECKBOX IS CLICKED   
    if st.checkbox('View Data'.upper()) :
        
        # SHOW DATA
        data = eda.showData()
        
         # DISPLAY DATAFRAME
        st.dataframe(data)
        
    # DISPLAY TEXT
    st.markdown(eda_text_2,unsafe_allow_html=True)    
        
    # IF CHECKBOX IS CLICKED   
    if st.checkbox('View Information about the data'.upper()) :
        
        # SHOW DATA
        data = eda.dataInfo()
        
         # DISPLAY DATAFRAME
        st.write(data)    
    
    # DISPLAY TEXT
    st.markdown(eda_text_3,unsafe_allow_html=True)    
        
    if st.checkbox('view features'.upper()) :
        
        # DISPLAY TEXT
        st.markdown(eda_text_4,unsafe_allow_html=True)    

def predictPage() :
    
    ''' FUNCTION TO CREATE PRICE PREDICTION PAGE'''
    
    # PAGE HEADER
    st.markdown(predict_header,unsafe_allow_html=True)
    
    # SPLITTING INTO # COLUMNS
    col1, col2, col3 = st.columns([2, 5, 2])
    
    # DISPLAY IMAGE
    imageAlignCenter(sell_image)
    
    ## INPUTS FOR OUR MODEL
    inp1 = st.text_input('Enter the minimum cost price of your vehicle : '.upper(),placeholder="ENTER THE MINIMUM COST PRICE VALUE IN RUPEES")
    
    inp2 = st.text_input('Enter the maximum cost price of your vehicle : '.upper(),placeholder="ENTER THE MAXIMUM COST PRICE VALUE IN RUPEES")
    
    inp3 = st.text_input('Enter the total distance travelled with your vehicle  : '.upper(),placeholder="ENTER THE DISTANCE VALUE IN KM")
    
    inp4 = st.text_input('Since how many years are you driving your vehicle : '.upper(),placeholder="ENTER THE VEHICLE AGE IN YEARS")
    
    inp5 = st.text_input('Enter your car\'s mileage : '.upper(),placeholder="ENTER THE MILEAGE VALUE IN KMPL")
    
    
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
        
        
        val = dis.validate(inp1,inp2,inp3,inp4,inp5)
        
        if val :
            
            st.warning('Please enter valid Inputs')
            
        else :
            
            data = [inp3,inp4,inp2,inp1,inp5]
            
            new_data = pp.preProcess(data)
            
            sell_price = pp.predictPrice(new_data)
            
            dis.displayOutput(sell_price)
        
    