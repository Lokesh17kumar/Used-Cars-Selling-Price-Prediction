''' PROGRAM TO VALIDATE INPUTS'''
import streamlit as st
import time
          

def displayOutput(sell_price) :
    
    ''' Function to display output ''' 
   
    #DISPLAY LOADING 
    with st.spinner('Analysing the selling price...'):
            
        # PAUSE EXECUTION    
        time.sleep(2)
                
        #DISPLAY OUTPUT
            
        st.success('The estimated selling price for your car is  :  {0} {1}'.format(sell_price,'\u20B9'))
         