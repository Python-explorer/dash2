import pandas as pd
import numpy as np
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

def generate_chart_1():
    url = 'https://raw.githubusercontent.com/Python-explorer/demodashboard/main/analysis/UHS65.csv'
    df = pd.read_csv(url)
    treatment_functions = df['Treatment Function'].loc[df['Treatment Function'] != 'Total']
    data = df.loc[df['Treatment Function'] != 'Total', :].iloc[:, 1:]
    p = figure(x_range=list(df.columns[1:]), plot_height=600, title="Number of Patients 65w+ UHSx by Treatment Function", x_axis_label="Month", y_axis_label="Number of Patients")
    source = ColumnDataSource(data)
    num_colors = len(treatment_functions)
    color_palette = ["#%06x" % np.random.randint(0, 0xFFFFFF) for _ in range(num_colors)]
    for i, treatment_function in enumerate(treatment_functions):
        p.line(df.columns[1:], data.iloc[i, :], line_color=color_palette[i], legend_label=treatment_function, line_width=2)
    p.add_layout(p.legend[0], 'left')
    p.legend.click_policy="hide"
    return p
