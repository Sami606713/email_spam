import streamlit as st
import pandas as pd
import numpy as np
from utils import prediction

def page_config():
    st.set_page_config(
        page_title="Email Spam Classifier",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def layout():
    col1,col2,col3=st.columns(3)
    with col1:
        pass

    with col2:
        st.subheader("Email Spam Classifier", divider='rainbow')

    with col3:
        pass


def main():
    # set the page config
    page_config()

    # Adjust the layout
    layout()

    # take the user input
    text=st.text_input("Enter text: ")
    
    # convert to dataframe
    dic={"text":text}
    df=pd.DataFrame(dic,index=[1])
    
    # Add the button
    if(st.button("classify")):
        pred=prediction(df['text'])[0]
        st.dataframe(df)
        if(pred==0):
            st.success(f"{text} are not a spam message")
        elif(pred==1):
            st.error(f"{text} is a spam message")

if __name__ =="__main__":
    main()