import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output

data_path  = "people-with-mental-health-disorders.csv"

df = pd.read_csv(data_path)

df["new_column"] = [0 for i in range(6156)]

print(df.head())

for i in df["Code"]:
    if i == 'AFG':
        print("success")