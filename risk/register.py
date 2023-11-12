import streamlit as st
import pandas as pd

st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)

def risk_table():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/Python-explorer/dash2/main/risk/data.csv')
    
    # Define a function to apply coloring to risk score
    def color_risk_score(val):
        if val >= 20:
            color = 'red'
        elif 11 <= val < 20:
            color = 'orange'
        else:
            color = 'green'
        return f'background-color: {color}; color: white;'

    # Apply the styling
    styled_df = df.style.applymap(color_risk_score, subset=['risk score'])\
        .set_properties(**{'background-color': 'grey', 'color': 'black'}, subset=pd.IndexSlice[0:0, :])\
        .set_table_styles([{'selector': 'th', 'props': [('background-color', 'grey'), ('color', 'black'), ('font-weight', 'bold')]}])
    
    # Display the DataFrame as a table in Streamlit with styling
    st.dataframe(styled_df)
