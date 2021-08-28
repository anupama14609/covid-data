import pandas as pd 
import numpy as np

df= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
contryNames=list(df['Country/Region'].values)

for i in contryNames:
    try:
        tempdf=df[df['Country/Region']==i]
        temp={}
        temp["name"]=i
        for j in tempdf[tempdf.columns[1:]].sum().index:
            for k in tempdf[tempdf.columns[1:]].sum().values:
                temp['x'] = j
                temp['y'] = k          
    except:
        pass

    context = {'name':temp['name'],'x':temp['x'], 'y': temp['y']}
    print(context)
