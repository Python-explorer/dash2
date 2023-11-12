import streamlit as st
import pandas as pd

import streamlit as st

def risk_table():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/Python-explorer/dash2/main/risk/data.csv')
    
    # Display the DataFrame as a table in Streamlit
    st.dataframe(df)
