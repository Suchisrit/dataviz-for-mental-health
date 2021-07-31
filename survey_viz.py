# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#47003e',
    'text': '#df0170'
}


data_path  = "survey.csv"
data = pd.read_csv(data_path)

oftenAll = data[data['work_interfere']=='Often']
oftenYes = oftenAll[oftenAll['treatment']=='Yes']
oftenPercent = (len(oftenYes) / len(oftenAll))
oftenAll['percentage'] = oftenAll['treatment'].astype('category').map({"Yes":"{}%".format(round(oftenPercent*100)), "No":"{}%".format(round((1-oftenPercent)*100))})

sometimesAll = data[data['work_interfere']=='Sometimes']
sometimesYes = sometimesAll[sometimesAll['treatment']=='Yes']
sometimesPercent = (len(sometimesYes) / len(sometimesAll))
sometimesAll['percentage'] = sometimesAll['treatment'].astype('category').map({"Yes":"{}%".format(round(sometimesPercent*100)), "No":"{}%".format(round((1-sometimesPercent)*100))})

rarelyAll = data[data['work_interfere']=='Rarely']
rarelyYes = rarelyAll[rarelyAll['treatment']=='Yes']
rarelyPercent = (len(rarelyYes) / len(rarelyAll))
rarelyAll['percentage'] = rarelyAll['treatment'].astype('category').map({"Yes":"{}%".format(round(rarelyPercent*100)), "No":"{}%".format(round((1-rarelyPercent)*100))})

neverAll = data[data['work_interfere']=='Never']
neverYes = neverAll[neverAll['treatment']=='Yes']
neverPercent = (len(neverYes) / len(neverAll))
neverAll['percentage'] = neverAll['treatment'].astype('category').map({"Yes":"{}%".format(round(neverPercent*100)), "No":"{}%".format(round((1-neverPercent)*100))})

frames = [neverAll, rarelyAll, sometimesAll, oftenAll]
result = pd.concat(frames)

# data['Severity'] = data['work_interfere'].astype('category').map({"Never":0, "Rarely":1, "Sometimes":2, "Often":3})

#fig = px.bar(data, x="Severity", color="treatment", range_x=[0, 3], )
fig = px.bar(result, x="work_interfere", color="treatment", range_y=[0, 501], category_orders={"work_interfere":["Never", "Rarely", "Sometimes", "Often"], "treatment":["Yes", "No"]}, hover_name='percentage', color_discrete_sequence=["rgb(116, 1, 223)", "rgb(223, 1, 46)"], labels={"work_interfere": "Frequency of Negative Mental Health Condition Effects", "count": "Amount of People", "treatment": "Did the individual<br>seek treatment?"})
'''
x = data['work_interfere']


fig = go.Figure(go.Bar(x=x, y=[len(often)], name='Yes'))
fig.add_trace(go.Bar(x=x, y=data[data['treatment']=='No'], name='No'))

fig.update_layout(barmode='stack')
fig.update_xaxes(categoryorder='category ascending')
'''

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    barmode='stack',
)

fig.update_traces(
    marker_line_width=0,
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Percentage of People that Seek Mental Health Treatment',
        style={
            'textAlign': 'center',
            'color': 'rgb(223, 1, 112)',
        }
    ),

    html.Div(children='', style={
        'textAlign': 'center',
        'color': 'red'
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)