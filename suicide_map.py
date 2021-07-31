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
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#ffffff',
    'text': '#7FDBFF'
}

data_path  = "people-with-mental-health-disorders.csv"

df = pd.read_csv(data_path)

df2 = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

df2[]



'''
fig = go.Figure(data=go.Choropleth(
    
    locations = df['Code'],
    z = df['Prevalence - Mental health disorders: Both (Number)'],
    text = df['Entity'],
    colorscale = [[0, '#D3394C'], [0.05, '#AF2D46'], [0.4, '#8B2444'], [0.6, '#722040'], [0.8, '#6A1C48'], [1, 'purple']],
    autocolorscale=False,
    reversescale=False,
    zmax=100000000,
    zmin=0,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_ticksuffix = '',
    colorbar_title = 'Amount of People',
))
#(data, x="Sex", y="2016", color="Country")#, range_y=[0, 8000000], color_continuous_scale=["blue", "green", "purple"])

fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    autosize=False,
    width=1300,
    height=800

)
'''
app.layout = html.Div([
    html.H1(
        children='Mental Health Disorders by Location',
        style={
            'textAlign': 'center',
            'color': 'purple'
        }
    ),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].min(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    ),

])

'''
style={'backgroundColor': colors['background']}, children=[

    html.Div(children='', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
'''

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df['Year'] == selected_year]

    # fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
    #                  size="pop", color="continent", hover_name="country",
    #                  log_x=True, size_max=55)

    # fig.update_layout(transition_duration=500)

    fig = go.Figure(data=go.Choropleth(
    
        locations = filtered_df['Code'],
        z = filtered_df['Prevalence - Mental health disorders: Both (Number)'],
        text = filtered_df['Entity'],
        colorscale = [[0, '#df6d7a'], [0.05, '#D3394C'], [0.1, '#AF2D46'], [0.15, '#8B2444'], [0.2, '#722040'], [0.25, '#6A1C48'], [1, 'purple']],
        autocolorscale=False,
        reversescale=False,
        zmax=10**8,
        zmin=0,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_ticksuffix = '',
        colorbar_title = 'Amount of People',
    ))
    #(data, x="Sex", y="2016", color="Country")#, range_y=[0, 8000000], color_continuous_scale=["blue", "green", "purple"])

    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        autosize=False,
        width=1300,
        height=800,
        transition_duration=1500

    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)