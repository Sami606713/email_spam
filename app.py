import streamlit as st
import pandas as pd
from utils import load_model

def page_config():
    st.set_page_config(
        page_title="Customer Churn Prediction",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def layout():
    col1,col2,col3=st.columns(3)
    with col1:
        pass

    with col2:
        st.subheader("Customrer Churn Prediction", divider='rainbow')

    with col3:
        pass

def main():
    page_config()
    layout()

if __name__ =="__main__":
    main()