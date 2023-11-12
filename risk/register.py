import streamlit as st
import pandas as pd

def risk_table():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/Python-explorer/dash2/main/risk/data.csv')
    
    # Define a function to apply coloring to 'Total risk score'
    def color_risk_score(val):
        color = 'green'  # default color
        if val >= 20:
            color = 'red'
        elif 11 <= val < 20:
            color = 'orange'
        return f'color: white; background-color: {color};'

    # Apply the styling
    styled_df = df.style.applymap(color_risk_score, subset=['Total risk score'])\
        .set_table_styles([{
            # This styles the header row
            'selector': 'thead th',
            'props': [('background-color', 'grey'), ('color', 'black'), ('font-weight', 'bold')]
        }])

    # Convert the styled DataFrame to HTML and display using st.markdown
    st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)

# Call the risk_table function to display the table
risk_table()
