import pandas as pd 
import numpy as np

df= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
contryNames=list(df['Country/Region'].values)

for i in contryNames:
    try:
        tempdf=df[df['Country/Region']==i]
        temp={}
        temp["name"]=i
        temp['data'] = [{'x':j,'y':k} for j,k in zip(
    tempdf[tempdf.columns[1:]].sum().index,tempdf[tempdf.columns[1:]].sum().values
    )]
    
    except:
        pass

    context = {
    'name':temp['name'],
    'data':temp['data']
    }
    print(context)

