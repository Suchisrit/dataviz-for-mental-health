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

data_path  = "people-with-mental-health-disorders copy.csv"

df = pd.read_csv(data_path)

df2 = pd.read_csv('WPP2019_TotalPopulationBySex.csv')

df2['Code'] = df2['Location'].astype('category').map({
    'Afghanistan': 'AFG',
    'Albania': 'ALB',
    'Algeria': 'DZA',
    'American Samoa': 'ASM',
    'Andorra': 'AND',
    'Angola': 'AGO',
    'Anguilla': 'AIA',
    'Antigua and Barbuda': 'ATG',
    'Argentina': 'ARG',
    'Armenia': 'ARM',
    'Aruba': 'ABW',
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Azerbaijan': 'AZE',
    'Bahamas, The': 'BHM',
    'Bahrain': 'BHR',
    'Bangladesh': 'BGD',
    'Barbados': 'BRB',
    'Belarus': 'BLR',
    'Belgium': 'BEL',
    'Belize': 'BLZ',
    'Benin': 'BEN',
    'Bermuda': 'BMU',
    'Bhutan': 'BTN',
    'Bolivia': 'BOL',
    'Bosnia and Herzegovina': 'BIH',
    'Botswana': 'BWA',
    'Brazil': 'BRA',
    'British Virgin Islands': 'VGB',
    'Brunei': 'BRN',
    'Bulgaria': 'BGR',
    'Burkina Faso': 'BFA',
    'Burma': 'MMR',
    'Burundi': 'BDI',
    'Cabo Verde': 'CPV',
    'Cambodia': 'KHM',
    'Cameroon': 'CMR',
    'Canada': 'CAN',
    'Cayman Islands': 'CYM',
    'Central African Republic': 'CAF',
    'Chad': 'TCD',
    'Chile': 'CHL',
    'China': 'CHN',
    'Colombia': 'COL',
    'Comoros': 'COM',
    'Congo': 'COD',
    'Cook Islands': 'COK',
    'Costa Rica': 'CRI',
    'Cote d\'Ivoire': 'CIV',
    'Croatia': 'HRV',
    'Cuba': 'CUB',
    'Curacao': 'CUW',
    'Cyprus': 'CYP',
    'Czech Republic': 'CZE',
    'Denmark': 'DNK',
    'Djibouti': 'DJI',
    'Dominica': 'DMA',
    'Dominican Republic': 'DOM',
    'Ecuador': 'ECU',
    'Egypt': 'EGY',
    'El Salvador': 'SLV',
    'Equatorial Guinea': 'GNQ',
    'Eritrea': 'ERI',
    'Estonia': 'EST',
    'Ethiopia': 'ETH',
    'Falkland Islands (Islas Malvinas)': 'FLK',
    'Faroe Islands': 'FRO',
    'Fiji': 'FJI',
    'Finland': 'FIN',
    'France': 'FRA',
    'French Polynesia': 'PYF',
    'Gabon': 'GAB',
    '"Gambia': '0.92,GMB',
    'Georgia': 'GEO',
    'Germany': 'DEU',
    'Ghana': 'GHA',
    'Gibraltar': 'GIB',
    'Greece': 'GRC',
    'Greenland': 'GRL',
    'Grenada': 'GRD',
    'Guam': 'GUM',
    'Guatemala': 'GTM',
    'Guernsey': 'GGY',
    'Guinea-Bissau': 'GNB',
    'Guinea': 'GIN',
    'Guyana': 'GUY',
    'Haiti': 'HTI',
    'Honduras': 'HND',
    'Hong Kong': 'HKG',
    'Hungary': 'HUN',
    'Iceland': 'ISL',
    'India': 'IND',
    'Indonesia': 'IDN',
    'Iran': 'IRN',
    'Iraq': 'IRQ',
    'Ireland': 'IRL',
    'Isle of Man': 'IMN',
    'Israel': 'ISR',
    'Italy': 'ITA',
    'Jamaica': 'JAM',
    'Japan': 'JPN',
    'Jersey': 'JEY',
    'Jordan': 'JOR',
    'Kazakhstan': 'KAZ',
    'Kenya': 'KEN',
    'Kiribati': 'KIR',
    'Kosovo': 'KSV',
    'Kuwait': 'KWT',
    'Kyrgyzstan': 'KGZ',
    'Laos': 'LAO',
    'Latvia': 'LVA',
    'Lebanon': 'LBN',
    'Lesotho': 'LSO',
    'Liberia': 'LBR',
    'Libya': 'LBY',
    'Liechtenstein': 'LIE',
    'Lithuania': 'LTU',
    'Luxembourg': 'LUX',
    'Macau': 'MAC',
    'Macedonia': 'MKD',
    'Madagascar': 'MDG',
    'Malawi': 'MWI',
    'Malaysia': 'MYS',
    'Maldives': 'MDV',
    'Mali': 'MLI',
    'Malta': 'MLT',
    'Marshall Islands': 'MHL',
    'Mauritania': 'MRT',
    'Mauritius': 'MUS',
    'Mexico': 'MEX',
    'Micronesia, Federated States of': 'FSM',
    'Moldova': 'MDA',
    'Monaco': 'MCO',
    'Mongolia': 'MNG',
    'Montenegro': 'MNE',
    'Morocco': 'MAR',
    'Mozambique': 'MOZ',
    'Namibia': 'NAM',
    'Nepal': 'NPL',
    'Netherlands': 'NLD',
    'New Caledonia': 'NCL',
    'New Zealand': 'NZL',
    'Nicaragua': 'NIC',
    'Nigeria': 'NGA',
    'Niger': 'NER',
    'Niue': 'NIU',
    'Northern Mariana Islands': 'MNP',
    'Norway': 'NOR',
    'Oman': 'OMN',
    'Pakistan': 'PAK',
    'Palau': 'PLW',
    'Panama': 'PAN',
    'Papua New Guinea': 'PNG',
    'Paraguay': 'PRY',
    'Peru': 'PER',
    'Philippines': 'PHL',
    'Poland': 'POL',
    'Portugal': 'PRT',
    'Puerto Rico': 'PRI',
    'Qatar': 'QAT',
    'Romania': 'ROU',
    'Russia': 'RUS',
    'Rwanda': 'RWA',
    'Saint Kitts and Nevis': 'KNA',
    'Saint Lucia': 'LCA',
    'Saint Martin': 'MAF',
    'Saint Pierre and Miquelon': 'SPM',
    'Saint Vincent and the Grenadines': 'VCT',
    'Samoa': 'WSM',
    'San Marino': 'SMR',
    'Sao Tome and Principe': 'STP',
    'Saudi Arabia': 'SAU',
    'Senegal': 'SEN',
    'Serbia': 'SRB',
    'Seychelles': 'SYC',
    'Sierra Leone': 'SLE',
    'Singapore': 'SGP',
    'Sint Maarten': 'SXM',
    'Slovakia': 'SVK',
    'Slovenia': 'SVN',
    'Solomon Islands': 'SLB',
    'Somalia': 'SOM',
    'South Africa': 'ZAF',
    'South Sudan': 'SSD',
    'Spain': 'ESP',
    'Sri Lanka': 'LKA',
    'Sudan': 'SDN',
    'Suriname': 'SUR',
    'Swaziland': 'SWZ',
    'Sweden': 'SWE',
    'Switzerland': 'CHE',
    'Syria': 'SYR',
    'Taiwan': 'TWN',
    'Tajikistan': 'TJK',
    'Tanzania': 'TZA',
    'Thailand': 'THA',
    'Timor-Leste': 'TLS',
    'Togo': 'TGO',
    'Tonga': 'TON',
    'Trinidad and Tobago': 'TTO',
    'Tunisia': 'TUN',
    'Turkey': 'TUR',
    'Turkmenistan': 'TKM',
    'Tuvalu': 'TUV',
    'Uganda': 'UGA',
    'Ukraine': 'UKR',
    'United Arab Emirates': 'ARE',
    'United Kingdom': 'GBR',
    'United States of America': 'USA',
    'Uruguay': 'URY',
    'Uzbekistan': 'UZB',
    'Vanuatu': 'VUT',
    'Venezuela': 'VEN',
    'Vietnam': 'VNM',
    'Virgin Islands': 'VGB',
    'West Bank': 'WBG',
    'Yemen': 'YEM',
    'Zambia': 'ZMB',
    'Zimbabwe': 'ZWE',
})


df2["population"] = df2["PopTotal"] * 1000

frames = []

for theYear in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]:
    print(theYear)
    blank = []
    yearlyDF = df[df['Year']==theYear]
    yearlyDF2 = df2[df2['Time']==theYear]
    print(yearlyDF["Code"])
    for i in yearlyDF["Code"]:
        print('i: ', i)
        for index in yearlyDF2.index:
            if i == yearlyDF2['Code'][index]:
                blank.append(yearlyDF2['PopTotal'][index])
                break

    yearlyDF["totalPop"] = blank
    frames.append(yearlyDF)

print("SUCCESS")
result = pd.concat(frames)
result["percentage"] = (result["Prevalence - Mental health disorders: Both (Number)"] / result["totalPop"]) * 100

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
        min=result['Year'].min(),
        max=result['Year'].max(),
        value=result['Year'].min(),
        marks={str(year): str(year) for year in result['Year'].unique()},
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
    filtered_df = result[result['Year'] == selected_year]

    # fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
    #                  size="pop", color="continent", hover_name="country",
    #                  log_x=True, size_max=55)

    # fig.update_layout(transition_duration=500)

    fig = go.Figure(data=go.Choropleth(
    
        locations = filtered_df['Code'],
        z = filtered_df['percentage'],
        text = filtered_df['Entity'],
        colorscale = [[0, '#df6d7a'], [0.05, '#D3394C'], [0.1, '#AF2D46'], [0.15, '#8B2444'], [0.2, '#722040'], [0.25, '#6A1C48'], [1, 'purple']],
        autocolorscale=False,
        reversescale=False,
        # zmax=10**8,
        # zmin=0,
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