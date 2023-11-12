import streamlit as st
import numpy as np
from bokeh.plotting import figure  # Make sure this import is included
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from analysis.charts import generate_chart_1

# Function to create empty placeholder charts
def create_placeholder_chart():
    categories = ['A', 'B', 'C', 'D', 'E']
    data = np.random.randint(1, 100, size=5)
    source = ColumnDataSource(data=dict(categories=categories, data=data))
    p = figure(x_range=categories, height=250, width=250, title="Random Bar Chart",
               toolbar_location=None, tools="")
    p.vbar(x='categories', top='data', width=0.9, source=source, color="navy")
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.outline_line_color = None
    return p

# Set the page config to wide mode
st.set_page_config(layout="wide", page_title="Demo Assurance Dashboard")

# Create the sidebar with radio buttons
st.sidebar.title('Demo Assurance Dashboard')
options = ['Headline Charts', 'Planned care', 'Urgent care', 'Mental health', 'General practice', 'Primary and community', 'Inequality', 'Risk', 'Insight']
selection = st.sidebar.radio("Choose a category", options)

# Main page content
if selection == 'Headline Charts':
    st.markdown("<h1 style='color: black;'>Headline Charts</h1>", unsafe_allow_html=True)

    # Use the imported function to create the first chart
    first_chart = generate_chart_1()

    # Generate placeholder charts for the rest of the grid
    placeholder_charts = [create_placeholder_chart() for _ in range(5)]
    
    # Combine the first chart with the placeholders into a single list
    all_charts = [first_chart] + placeholder_charts

    # Arrange the charts in two columns and three rows
    grid = gridplot(all_charts, ncols=2, sizing_mode='scale_width')
    st.bokeh_chart(grid)

elif selection == 'Risk':
    # Call the function from register.py to get the DataFrame
    risk_table = risk_table()
    # Display the table in Streamlit
    st.table(risk_table)
    
else:
    # For other selections, you can add appropriate content here
    st.write(f"You selected: {selection}")
