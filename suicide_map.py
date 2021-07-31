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

'''
df2['Code'] = df2['Location'].astype('category').map({

})
'''


df2['Code'] = df2['Location'].astype('category').map({
    'Aruba': 'ABW',
    'Afghanistan': 'AFG',
    'Angola': 'AGO', 
    'Anguilla': 'AIA', 
    'Åland Islands': 'ALA', 
    'Albania': 'ALB', 
    'Andorra': 'AND', 
    'Netherlands Antilles': 'ANT', 
    'United Arab Emirates': 'ARE', 
    'Argentina': 'ARG', 
    'Armenia': 'ARM', 
    'American Samoa': 'ASM', 
    'Antarctica': 'ATA', 
    'French Southern Territories': 'ATF', 
    'Antigua and Barbuda': 'ATG', 
    'Australia': 'AUS', 
    'Austria': 'AUT', 
    'Azerbaijan': 'AZE', 
    'Burundi': 'BDI', 
    'Belgium': 'BEL', 
    'Benin': 'BEN', 
    'Burkina Faso': 'BFA', 
    'Bangladesh': 'BGD', 
    'Bulgaria': 'BGR', 
    'Bahrain': 'BHR', 
    'Bahamas': 'BHS', 
    'Bosnia and Herzegovina': 'BIH', 
    'Saint Barthélemy': 'BLM', 
    'Belarus': 'BLR', 
    'Belize': 'BLZ', 
    'Bermuda': 'BMU', 
    'Bolivia, Plurinational State of': 'BOL', 
    'Brazil': 'BRA', 
    'Barbados': 'BRB', 
    'Brunei Darussalam': 'BRN', 
    'Bhutan': 'BTN', 
    'Bouvet Island': 'BVT', 
    'Botswana': 'BWA', 
    'Central African Republic': 'CAF', 
    'Canada': 'CAN', 
    'Cocos (Keeling) Islands': 'CCK', 
    'Switzerland': 'CHE', 
    'Chile': 'CHL', 
    'China': 'CHN', 
    'Côte d\'Ivoire': 'CIV', 
    'Cameroon': 'CMR', 
    'Democratic Republic of Congo': 'COD', 
    'Congo': 'COG', 
    'Cook Islands': 'COK', 
    'Colombia': 'COL', 
    'Comoros': 'COM', 
    'Cape Verde': 'CPV', 
    'Costa Rica': 'CRI', 
    'Cuba': 'CUB', 
    'Christmas Island': 'CXR', 
    'Cayman Islands': 'CYM', 
    'Cyprus': 'CYP', 
    'Czech Republic': 'CZE', 
    'Czechia': 'CZE', 
    'Germany': 'DEU', 
    'Djibouti': 'DJI', 
    'Dominica': 'DMA', 
    'Denmark': 'DNK', 
    'Dominican Republic': 'DOM', 
    'Algeria': 'DZA', 
    'Ecuador': 'ECU', 
    'Egypt': 'EGY', 
    'Eritrea': 'ERI', 
    'Western Sahara': 'ESH', 
    'Spain': 'ESP', 
    'Estonia': 'EST', 
    'Eswatini': 'SWZ',
    'Ethiopia': 'ETH', 
    'Finland': 'FIN', 
    'Fiji': 'FJI', 
    'Falkland Islands (Malvinas)': 'FLK', 
    'France': 'FRA', 
    'Faroe Islands': 'FRO', 
    'Micronesia (country)': 'FSM', 
    'Gabon': 'GAB', 
    'United Kingdom': 'GBR', 
    'Georgia': 'GEO', 
    'Guernsey': 'GGY', 
    'Ghana': 'GHA', 
    'Gibraltar': 'GIB', 
    'Guinea': 'GIN', 
    'Guadeloupe': 'GLP', 
    'Gambia': 'GMB', 
    'Guinea-Bissau': 'GNB', 
    'Equatorial Guinea': 'GNQ', 
    'Greece': 'GRC', 
    'Grenada': 'GRD', 
    'Greenland': 'GRL', 
    'Guatemala': 'GTM', 
    'French Guiana': 'GUF', 
    'Guam': 'GUM', 
    'Guyana': 'GUY', 
    'Hong Kong': 'HKG', 
    'Heard Island and McDonald Islands': 'HMD', 
    'Honduras': 'HND', 
    'Croatia': 'HRV', 
    'Haiti': 'HTI', 
    'Hungary': 'HUN', 
    'Indonesia': 'IDN', 
    'Isle of Man': 'IMN', 
    'India': 'IND', 
    'British Indian Ocean Territory': 'IOT', 
    'Ireland': 'IRL', 
    'Iran, Islamic Republic of': 'IRN', 
    'Iraq': 'IRQ', 
    'Iceland': 'ISL', 
    'Israel': 'ISR', 
    'Italy': 'ITA', 
    'Jamaica': 'JAM', 
    'Jersey': 'JEY', 
    'Jordan': 'JOR', 
    'Japan': 'JPN', 
    'Kazakhstan': 'KAZ', 
    'Kenya': 'KEN', 
    'Kyrgyzstan': 'KGZ', 
    'Laos': 'LAO',
    'Cambodia': 'KHM', 
    'Kiribati': 'KIR', 
    'Saint Kitts and Nevis': 'KNA', 
    'South Korea': 'KOR', 
    'Kuwait': 'KWT', 
    'Lebanon': 'LBN', 
    'Liberia': 'LBR', 
    'Libyan Arab Jamahiriya': 'LBY', 
    'Saint Lucia': 'LCA', 
    'Liechtenstein': 'LIE', 
    'Sri Lanka': 'LKA', 
    'Lesotho': 'LSO', 
    'Lithuania': 'LTU', 
    'Luxembourg': 'LUX', 
    'Latvia': 'LVA', 
    'Macao': 'MAC', 
    'Saint Martin (French part)': 'MAF', 
    'Morocco': 'MAR', 
    'Monaco': 'MCO', 
    'Moldova': 'MDA', 
    'Madagascar': 'MDG', 
    'Maldives': 'MDV', 
    'Mexico': 'MEX', 
    'Marshall Islands': 'MHL', 
    'North Macedonia': 'MKD', 
    'Mali': 'MLI', 
    'Malta': 'MLT', 
    'Myanmar': 'MMR', 
    'Montenegro': 'MNE', 
    'Mongolia': 'MNG', 
    'Northern Mariana Islands': 'MNP', 
    'Mozambique': 'MOZ', 
    'Mauritania': 'MRT', 
    'Montserrat': 'MSR', 
    'Martinique': 'MTQ', 
    'Mauritius': 'MUS', 
    'Malawi': 'MWI', 
    'Malaysia': 'MYS', 
    'Mayotte': 'MYT', 
    'Namibia': 'NAM', 
    'New Caledonia': 'NCL', 
    'Niger': 'NER', 
    'Norfolk Island': 'NFK', 
    'Nigeria': 'NGA', 
    'Nicaragua': 'NIC', 
    'Niue': 'NIU', 
    'Netherlands': 'NLD', 
    'Norway': 'NOR', 
    'Nepal': 'NPL', 
    'Nauru': 'NRU', 
    'New Zealand': 'NZL', 
    'Oman': 'OMN', 
    'Pakistan': 'PAK', 
    'Panama': 'PAN', 
    'Pitcairn': 'PCN', 
    'Peru': 'PER', 
    'Philippines': 'PHL', 
    'Palau': 'PLW', 
    'Papua New Guinea': 'PNG', 
    'Poland': 'POL', 
    'Puerto Rico': 'PRI', 
    'North Korea': 'PRK', 
    'Portugal': 'PRT', 
    'Paraguay': 'PRY', 
    'Palestine': 'PSE', 
    'French Polynesia': 'PYF', 
    'Qatar': 'QAT', 
    'Réunion': 'REU', 
    'Romania': 'ROU', 
    'Russia': 'RUS', 
    'Rwanda': 'RWA', 
    'Saudi Arabia': 'SAU', 
    'South Sudan': 'SSD', 
    'Sudan': 'SDN', 
    'Senegal': 'SEN', 
    'Singapore': 'SGP', 
    'South Georgia and the South Sandwich Islands': 'SGS', 
    'Saint Helena, Ascension and Tristan da Cunha': 'SHN', 
    'Svalbard and Jan Mayen': 'SJM', 
    'Solomon Islands': 'SLB', 
    'Sierra Leone': 'SLE', 
    'El Salvador': 'SLV', 
    'San Marino': 'SMR', 
    'Somalia': 'SOM', 
    'Saint Pierre and Miquelon': 'SPM', 
    'Serbia': 'SRB', 
    'Sao Tome and Principe': 'STP', 
    'Suriname': 'SUR', 
    'Slovakia': 'SVK', 
    'Slovenia': 'SVN', 
    'Sweden': 'SWE', 
    'Swaziland': 'SWZ', 
    'Seychelles': 'SYC', 
    'Syria': 'SYR', 
    'Turks and Caicos Islands': 'TCA', 
    'Chad': 'TCD', 
    'Togo': 'TGO', 
    'Thailand': 'THA', 
    'Tajikistan': 'TJK', 
    'Tokelau': 'TKL', 
    'Turkmenistan': 'TKM', 
    'Timor': 'TLS', 
    'Tonga': 'TON', 
    'Trinidad and Tobago': 'TTO', 
    'Tunisia': 'TUN', 
    'Turkey': 'TUR', 
    'Tuvalu': 'TUV', 
    'Taiwan': 'TWN', 
    'Tanzania': 'TZA', 
    'Uganda': 'UGA', 
    'Ukraine': 'UKR', 
    'United States Minor Outlying Islands': 'UMI', 
    'Uruguay': 'URY', 
    'United States': 'USA', 
    'Uzbekistan': 'UZB', 
    'Holy See (Vatican City State)': 'VAT', 
    'Saint Vincent and the Grenadines': 'VCT', 
    'Venezuela': 'VEN', 
    'Virgin Islands, British': 'VGB', 
    'United States Virgin Islands': 'VIR', 
    'Vietnam': 'VNM', 
    'Vanuatu': 'VUT', 
    'Wallis and Futuna': 'WLF', 
    'Samoa': 'WSM', 
    'Yemen': 'YEM', 
    'South Africa': 'ZAF', 
    'Zambia': 'ZMB', 
    'Zimbabwe': 'ZWE',
})


df2["population"] = df2["PopTotal"] * 1000

frames = []

for theYear in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]:
    print(theYear)
    blank = []
    yearlyDF = df[df['Year']==theYear]
    for i in yearlyDF['Entity']:
        print('country: ', i)
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