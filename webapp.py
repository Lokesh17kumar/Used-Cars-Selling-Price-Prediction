import streamlit as st
import webpages as page

menu_name = "Navigation".upper()

menu_items = ['Home','EDA','Predict Price']

st.set_page_config(layout="wide")

def main() :
    
    ''' Function to start our program'''

    # NAVIGATION BAR
    navigation_bar = st.sidebar.radio(menu_name,menu_items)

    # IF 'Home' IS SELECTED IN NAVIGATION BAR
    if navigation_bar == 'Home':
    
        # CALLING 'homePage()' from 'webpages' module
        page.homePage()
    
    # IF 'EDA' IS SELECTED IN NAVIGATION BAR    
    if navigation_bar == 'EDA':
    
        # CALLING 'edaPage()' from 'webpages' module
        page.edaPage()
    
    # IF 'Price Predict' IS SELECTED IN NAVIGATION BAR    
    if navigation_bar == 'Predict Price':
    
        page.predictPage()

if __name__ == '__main__' :

    main()        
