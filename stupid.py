import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

data_path  = "survey.csv"

data = pd.read_csv(data_path)





oftenAll = data[data['work_interfere']=='Often']

oftenYes = oftenAll[oftenAll['treatment']=='Yes']

oftenPercent = (len(oftenYes) / len(oftenAll))

print(oftenPercent)






sometimesAll = data[data['work_interfere']=='Sometimes']

sometimesYes = sometimesAll[sometimesAll['treatment']=='Yes']

sometimesPercent = (len(sometimesYes) / len(sometimesAll))

print(sometimesPercent)






rarelyAll = data[data['work_interfere']=='Rarely']

rarelyYes = rarelyAll[rarelyAll['treatment']=='Yes']

rarelyPercent = (len(rarelyYes) / len(rarelyAll))

print(rarelyPercent)






neverAll = data[data['work_interfere']=='Never']

neverYes = neverAll[neverAll['treatment']=='Yes']

neverPercent = (len(neverYes) / len(neverAll))

print(neverPercent)