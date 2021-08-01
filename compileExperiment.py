import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
import glob
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


###################################################
#####         TECH SURVEY                      ####
###################################################



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

fig = px.bar(result, x="work_interfere", color="treatment", range_y=[0, 501], category_orders={"work_interfere":["Never", "Rarely", "Sometimes", "Often"], "treatment":["Yes", "No"]}, hover_name='percentage', color_discrete_sequence=["#004DA1", "#F5A627"], labels={"work_interfere": "Frequency of Negative Mental Health Condition Effects", "count": "Amount of People", "treatment": "Did the individual<br>seek treatment?"})

fig.update_layout(
    # plot_bgcolor='white',
    # paper_bgcolor='white',
    barmode='stack',
)

fig.update_traces(
    marker_line_width=0,
)


###########################################################
######            SUNBURST CHART                     ######
###########################################################


data_path2  = "Mental Health Data.csv"

dfSTI = pd.read_csv(data_path2)

dfSTI['Would you be willing to share with you friends and family that you have a mental illness?'] = dfSTI['How willing would you be to share with friends and family that you have a mental illness?'].astype('category').map({
    "Somewhat open":"Probably",
    "Very open":"Yes",
    "Somewhat not open":"Probably not",
    "Neutral":"Neutral",
    "Not open at all":"No",
    "Not applicable to me (I do not have a mental illness)":"N/A"
})

fig2 = px.sunburst(
    dfSTI,
    path=['Do you currently have a mental health disorder?', 'Would you be willing to share with you friends and family that you have a mental illness?'],
    labels={'Do you currently have a mental health disorder?': 'Do you currently have a mental health disorder?'},
    color='Do you currently have a mental health disorder?',
    color_discrete_sequence=['rgb(213, 102, 100)', 'rgb(11, 20, 20)', 'rgb(102, 123, 0)'],
    maxdepth=-1,
    hover_data=['Do you currently have a mental health disorder?', 'Would you be willing to share with you friends and family that you have a mental illness?'],
    branchvalues="remainder",
)

sizes = [35, 20, 20, 20, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 50, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

fig2.update_traces(
    go.Sunburst(

        hovertemplate = 
            'Would you be willing to share with you friends and family that you have a mental illness? : %{customdata[1]}' + 
            '<br>Count: %{value}'
    ),
    insidetextfont = dict(size=sizes)
)

fig2.update_layout(
    autosize=False,
    width=1000,
    height=600,
)



###########################################################
######            MENTAL HEALTH MAP                  ######
###########################################################



data_path3  = "people-with-mental-health-disorders copy.csv"

df = pd.read_csv(data_path3)

df2 = pd.read_csv('WPP2019_TotalPopulationBySex.csv')


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
    'Bolivia (Plurinational State of)': 'BOL', 
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
    'Democratic Republic of the Congo': 'COD', 
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
    'Iran (Islamic Republic of)': 'IRN', 
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
    'Lao People\'s Democratic Republic': 'LAO',
    'Cambodia': 'KHM', 
    'Kiribati': 'KIR', 
    'Saint Kitts and Nevis': 'KNA', 
    'Republic of Korea': 'KOR', 
    'Kuwait': 'KWT', 
    'Lebanon': 'LBN', 
    'Liberia': 'LBR', 
    'Libya': 'LBY', 
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
    'Dem. People\'s Republic of Korea': 'PRK', 
    'Portugal': 'PRT', 
    'Paraguay': 'PRY', 
    'Palestine': 'PSE', 
    'French Polynesia': 'PYF', 
    'Qatar': 'QAT', 
    'Réunion': 'REU', 
    'Romania': 'ROU', 
    'Russian Federation': 'RUS', 
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
    'United Republic of Tanzania': 'TZA', 
    'Uganda': 'UGA', 
    'Ukraine': 'UKR', 
    'United States Minor Outlying Islands': 'UMI', 
    'Uruguay': 'URY', 
    'United States of America': 'USA', 
    'Uzbekistan': 'UZB', 
    'Holy See (Vatican City State)': 'VAT', 
    'Saint Vincent and the Grenadines': 'VCT', 
    'Venezuela (Bolivarian Republic of)': 'VEN', 
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

frames2 = []

for theYear in range(1990, 2017):
    blank = []
    yearlyDF = df[df['Year']==theYear]
    yearlyDF2 = df2[df2['Time']==theYear]
    for i in yearlyDF["Code"]:
        for index in yearlyDF2.index:
            if i == yearlyDF2['Code'][index]:
                blank.append(yearlyDF2['population'][index])
                break

    yearlyDF["totalPop"] = blank
    frames2.append(yearlyDF)

print("SUCCESS")
result2 = pd.concat(frames2)
result2["percentage"] = (result2["Prevalence - Mental health disorders: Both (Number)"] / result2["totalPop"]) * 100



##################################################
######           LAYOUT                     ###### 
##################################################


image_directory = '/home/antz/vscode/Web/dataviz-for-mental-health/images/'
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
static_image_route = '/static/'

image_filename = 'images/mental-health.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


app.layout = html.Div(children=[

    html.H5(children='Data Viz for Mental Health', className="header"),

    html.Div([
        html.Div([
            html.H2(children='It\'s time to talk about', className="pre-bold-header"),
            html.H2(children='mental health.', className="post-bold-header"),

        ], className="left-side-hero"),
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), className='hero_img'),
    ], className="hero"),

    html.Div([
        html.P(children='With the pandemic looming overhead and Simone Biles\' Withdrawal from the Olympics, more attention is being drawn towards the issue of mental health in recent times'),
    ], className="transition-p"),

    html.Hr(className='transition-hr'),

    html.Div([
        html.Div([
            html.H2(children='The problem is that mental health isn\'t being treated enough as an illness or as a serious problem.', className="section-header"),
            html.P(children='Take a second to think about the people that you see everyday, and the people you don’t see often. According to the National Alliance on Mental Illness, 20.6% of US adults experienced an illness related to mental health in 2019. This means that 1 in 5 of all US adults were experiencing mental health issues. Think again about the friends and loved ones you were thinking about.', className="section-info"),
        ]),
        html.Hr(className='transition-mini-hr'),
        html.P(children='Here\'s a look at our first visualization. This is a graph of the percentage of population with mental health disorders for every country.', className="section-info"),

        html.Div([
            html.H5(children='Mental Health Disorders by Location'),
            dcc.Graph(id='graph-with-slider'),
            dcc.Slider(
                id='year-slider',
                min=result2['Year'].min(),
                max=result2['Year'].max(),
                value=result2['Year'].min(),
                marks={str(year): str(year) for year in result2['Year'].unique()},
                step=None
            ),  
        ], className='viz-1'),

        html.P(children='It\'s getting worse every year - not enough efforts are being undertaken to fight mental health disorders and to treat mental health. Not enough awareness?', className="section-info"),
    ], className='section'),

    html.Hr(className='transition-hr'),

    html.Div([
        html.Div([
            html.H2(children='Header 2', className="section-header"),
            html.P(children='Our next visualization utilizes survey data to take a closer look at the stigma surrounding mental health. The most common response tot he question blah', className="section-info"),
        ]),
        html.Hr(className='transition-mini-hr'),
        html.P(children='Yeet', className="section-info"),

        html.Div([
            html.H5(children='Do you currently have a mental health disorder?'),
            dcc.Graph(
                id='graph2',
                figure=fig2
            ),  
        ], className='viz-2'),

        html.P(children='yeet 2', className="section-info"),
    ], className='section'),

    html.Hr(className='transition-hr'),

    html.Div([
        html.Div([
            html.H2(children='Thankfully, some people are taking the care they need.', className="section-header"),
            html.P(children='Take a look at this bar graph for people in teh tech industry seeking mental health treatment.', className="section-info"),
        ]),
        html.Hr(className='transition-mini-hr'),
        html.P(children='our last data visualization uses a (link) kaggle dataset on survey responses for mental health in the tech industry.', className="section-info"),

        html.Div([
            html.H5(children='Frequency of Negative Mental Health Condition Effects'),
            dcc.Graph(
                id='graph1',
                figure=fig
            ),  
        ], className='viz-3'),

        html.P(children='yeet 3', className="section-info"),
    ], className='section'),
])


########################################################
######              CALLBACKS                   ########
########################################################


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = result2[result2['Year'] == selected_year]

    fig3 = go.Figure(data=go.Choropleth(
    
        locations = filtered_df['Code'],
        z = filtered_df['percentage'],
        text = ['Country: {} <br>Disorder Count: {} <br>Total Population: {}'.format(filtered_df["Entity"][i], int(filtered_df['Prevalence - Mental health disorders: Both (Number)'][i]), int(filtered_df['totalPop'][i])) for i in filtered_df.index],
        colorscale = [[0, "green"], [0.4, "green"], [0.6, "yellow"], [1, "yellow"]],
        autocolorscale=False,
        reversescale=False,
        zmax=26,
        zmin=0,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_ticksuffix = '%',
        colorbar_title = 'Percentage of Population',
        hovertemplate = 
            '<b>%{z:.2f}%</b>' +
            '<br>%{text}'
    ))

    fig3.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        autosize=False,
        width=970,
        height=500,
        transition_duration=1500,
        margin=dict(t=0, r=0, l=0, b=0)
    )

    return fig3




if __name__ == '__main__':
    app.run_server(debug=True)



