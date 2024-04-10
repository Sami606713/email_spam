import streamlit as st
import pandas as pd
import pickle as pkl

def load_model():
    with open('spam_cls.pkl','rb') as f:
        model=pkl.load(f)
    return model