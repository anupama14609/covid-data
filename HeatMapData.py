import pandas as pd 
import numpy as np

def HeatMapData(confirmedGlobal,contryNames):
    df3=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list(list(confirmedGlobal.columns.values)[-6:-1])]
    print("\n Heat Map DF")
    print(df3)
    
    dataForheatMap=[]
    for i in contryNames:
        try:
            tempdf=df3[df3['Country/Region']==i]
            temp={}
            temp["name"]=i
            temp["data"]=[{'x':j,'y':k} for j,k in zip(tempdf[tempdf.columns[1:]].sum().index,tempdf[tempdf.columns[1:]].sum().values)]
            dataForheatMap.append(temp)
        except:
            pass
    dateCat = list(list(confirmedGlobal.columns.values)[-6:-1])
  
    return dataForheatMap,dateCat

def Compile_HeatMapData():
    confirmedGlobal= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    uniqueCountryNames = pd.unique(confirmedGlobal['Country/Region']) 
    contryNames=list(confirmedGlobal['Country/Region'].values)
    dataForheatMap,dateCat = HeatMapData(confirmedGlobal,contryNames)

    print("\n uniqueCountryNames..........................")
    print(uniqueCountryNames)

    print("\n contryNames..........................")
    print(contryNames)

    print("\n dataForheatMap..........................")
    print(dataForheatMap)

    print("\n dateCat..........................")
    print(dateCat)

Compile_HeatMapData()
