import streamlit as st
import pandas as pd

def risk_table():
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('https://raw.githubusercontent.com/Python-explorer/dash2/main/risk/data.csv')
    
    # Define a function to apply coloring to risk score
    def color_risk_score(val):
        color = 'green'  # default color
        if val >= 20:
            color = 'red'
        elif 11 <= val < 20:
            color = 'orange'
        # Note: 'white' text color for readability
        return f'color: white; background-color: {color};'

    # Apply the styling
    styled_df = df.style.applymap(color_risk_score, subset=['risk score'])\
        .set_table_styles([{
            'selector': 'th',
            'props': [('background-color', 'grey'), ('color', 'black'), ('font-weight', 'bold')]
        }, {
            # Ensure index cells (headers of rows) are also styled
            'selector': '.index_name',
            'props': [('display', 'none')]  # This hides the index name if it's showing
        }, {
            'selector': '.row_heading',
            'props': [('background-color', 'grey'), ('color', 'black')]
        }, {
            'selector': '.blank',
            'props': [('background-color', 'grey'), ('color', 'black')]
        }])

    # Convert the styled DataFrame to HTML and display using st.markdown
    st.markdown(styled_df.to_html(escape=False), unsafe_allow_html=True)

# Call the risk_table function to display the table
risk_table()
