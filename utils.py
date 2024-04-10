import streamlit as st
import pandas as pd
import pickle as pkl

def load_model():
    try:
        
        with open('spam_cls.pkl','rb') as f:
            model=pkl.load(f)
        return model
    except FileNotFoundError as e:
        return e

def prediction(user_input):
    # Load the model
    model=load_model()

    # make the prediction
    pred=model.predict(user_input)
    return pred
