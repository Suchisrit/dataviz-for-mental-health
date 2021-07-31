import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
import plotly.express as px
import pandas as pd
import base64
import glob

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

image_directory = '/home/antz/vscode/Web/dataviz-for-mental-health/images/'
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
print(list_of_images)
static_image_route = '/static/'

image_filename = 'images/mental-health.png'
# image_filename = 'images/mental-health.svg'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

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
        html.H2(children='With Simone Biles’ withdrawal from the Olympics, more attention is being drawn towards the issue of mental health.')
    ]),

    html.Div([
        html.H2(children='The problem is that mental health isn’t being treated as an illness or as a serious problem. Here’s why: '),
        html.H2(children='SOMETHING ABOUT HOW PEOPLE DON’T CARE ABOUT IT')
    ]),

    html.Div([
        html.H2(children='Here’s a graph of mental health disorders in every country.'),
        html.H2(children='It’s getting worse every year -- not enough efforts are being undertaken to fight mental health disorders and treat mental health. Not enough awareness?')
    ]),

    html.Div([
        html.H2(children='We are seeing more and more articles published that mention mental health however bruh how does this fit in')
    ]),

    html.Div([
        html.H2(children='Thankfully, some people are taking the care they need. take a look at this bar graph for people in the tech industry and seeking mental health treatment.')
    ]),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# @app.callback(
#     dash.dependencies.Output('image', 'src'),
#     [dash.dependencies.Input('image-dropdown', 'value')])
# def update_image_src(value):
#     return static_image_route + value

@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_image(image_path):
    image_name = '{}.png'.format(image_path)
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)

if __name__ == '__main__':
    app.run_server(debug=True)