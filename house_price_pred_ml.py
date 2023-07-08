import pandas as pd
import streamlit as st

import pickle

housing= pd.read_csv(r"E:\ml2\housing\Housing.csv")
housing.head()

st.write("""
#  Magic Bricks house Price Prediction
""")