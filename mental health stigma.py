# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

data_path  = "Mental Health Data.csv"

df = pd.read_csv(data_path)

df['Would you be willing to share with you friends and family that you have a mental illness?'] = df['How willing would you be to share with friends and family that you have a mental illness?'].astype('category').map({
    "Somewhat open":"Probably",
    "Very open":"Yes",
    "Somewhat not open":"Probably not",
    "Neutral":"Neutral",
    "Not open at all":"No",
    "Not applicable to me (I do not have a mental illness)":"N/A"
})

fig = px.sunburst(
    df,
    path=['Do you currently have a mental health disorder?', 'Would you be willing to share with you friends and family that you have a mental illness?'],
    labels={'Do you currently have a mental health disorder?': 'Do you currently have a mental health disorder?'},
    color='Do you currently have a mental health disorder?',
    color_discrete_sequence=['rgb(213, 102, 100)', 'rgb(11, 20, 20)', 'rgb(102, 123, 0)'],
    maxdepth=-1,
    hover_data=['Do you currently have a mental health disorder?', 'Would you be willing to share with you friends and family that you have a mental illness?'],
    branchvalues="remainder",
)

sizes = [35, 20, 20, 20, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

fig.update_traces(
    go.Sunburst(

        hovertemplate = 
            'Do you currently have a mental health disorder? : %{customdata[0]}' + 
            '<br>Would you be willing to share with you friends and family that you have a mental illness? : %{customdata[1]}' + 
            '<br>Count: %{value}'
        # hoverinfo="none"
    ),
    insidetextfont = dict(size=sizes)
)

fig.update_layout(
    autosize=False,
    width=1300,
    height=800,
)



# text = []

# for w in fig.data[0].ids:
#     if '/'  not in w:
#         text.append(f'Country: {w}')
#     else:
#         sw = w.split('/')
#         if len(sw) == 2:
#             text.append(f'Country: {sw[0]}<br>Year: {sw[1]}')
#         elif len(sw) == 3:
#             text.append(f'Country: {sw[0]}<br>Year: {sw[1]}<br>Attacks: {sw[2]}')
#         elif len(sw) == 4:
#             text.append(f'Country: {sw[0]}<br>Year: {sw[1]}<br>Attacks: {sw[2]}<br>Killed: {sw[3]}')
#         else: pass  




# fig.update_traces(
#     text=text, 
#     textinfo='text',
#     hoverinfo='text',
#     hovertemplate=None)

app.layout = html.Div(children=[
    html.H1(children='Do you currently have a mental health disorder?'),


    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)