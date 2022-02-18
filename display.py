''' PROGRAM TO VALIDATE INPUTS'''
import streamlit as st
import time


def spaceCheck(inp) :
    
    ''' Function to check for space'''
    
    if  (inp == '') :
            
        st.warning('Please Do not leave the field(s) empty') 
        
        return True      
        
    if  (inp == ' ') :
            
        st.warning('Please Do not give space as the input')       

        return True

def currencyCheck(inp) :
    
    ''' Function to check for currency'''
    
    char = ','
    
    if char in inp :
        
        return True    

def isFloat(inp) :
    
    ''' Function to check if input is float'''
    try :
        
        float(inp)
        
        return True
    
    except ValueError :
        
        return False


def typeCheck(inp) :
    
    ''' Function to check type of the input'''
    
    if not( (inp.isnumeric()) or (isFloat(inp)) or (currencyCheck(inp)) ):
        
       st.warning('Please do no enter text or characters in the input(s)')
       
       return True 
        

def negCheck(inp) :
    
    ''' Function to check if input is negative''' 
    
    try :
        
        if int(inp) < 0 :
            
            st.warning('Please do not enter negative value(s)')
            
            return True
        
        else : 
            
            return False
    
    except ValueError :
        
        return False    
        

def validate(inp1,inp2,inp3,inp4,inp5) :
    
    # STORE INPUTS INTO A LIST
    data = [inp1,inp2,inp3,inp4,inp5]

    # TO CHECK IF INPUTS ARE EMPTY
    if data == None :
        
        # PROMPT MESSAGE
        st.warning('Please Enter the Input(s)')
    
    else :    

        
        for inp in data :
        
            
            if spaceCheck(inp) :
                
                return 1
            
            if typeCheck(inp) :
                
                return 1
            
            if negCheck(inp) :
                
                return 1
            

def displayOutput(sell_price,val=4) :
    
    ''' Function to display output ''' 
   
    #DISPLAY LOADING 
    with st.spinner('Analysing the selling price...'):
                
        time.sleep(2)
                
        #DISPLAY OUTPUT
            
        st.success('The estimated selling price for your car is  :  {0} {1}'.format(sell_price,'\u20B9'))
         