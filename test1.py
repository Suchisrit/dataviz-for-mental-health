import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

suicide_data_path  = "Age-standardized suicide rates.csv"
survey_data_path  = "survey.csv"

suicideData = pd.read_csv(suicide_data_path)
surveyData = pd.read_csv(survey_data_path)

print(suicideData.head())
print(surveyData.head())