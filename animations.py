import json

def loadLottie(path) :
    
    ''' Function to display animations'''
    
    with open(path,'r') as file :
        
        return json.load(file)