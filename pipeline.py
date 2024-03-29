import pickle
import pandas as pd
import numpy as np

with open(r'model.pkl','rb') as model_file:

    model = pickle.load(model_file)
    
def preProcess(data) :
    
    ''' Function to pre-process data'''
    
    
    # CHANGING DATA TYPE TO FLOAT
    for ind , val in enumerate(data) :
        
        data[ind] = float(val)
    
    # CHANGING TO ARRAY
    data = (np.array(data)).reshape(1,-1)     
                                   
    return data        
    
def predictPrice(data) :
    
    ''' Function to predict price'''
    
    sell_price = round(model.predict(data)[0] , 3)
    
    result = '{:,}'.format(sell_price)
    
    return result