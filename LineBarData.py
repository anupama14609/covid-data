import pandas as pd 
import numpy as np

confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
uniqueCountryNames=pd.unique(confirmedGlobal['Country/Region']) 

def LineBarData(confirmedGlobal):
    df2=confirmedGlobal[list(confirmedGlobal.columns[1:2])+list([confirmedGlobal.columns[-2]])]
    df2.columns=['Country/Region','values']
    df2=df2.sort_values(by='values',ascending=False)
    contryNames=list(df2['Country/Region'].values)
    countsVal=list(df2['values'].values)
    maxVal=max(countsVal)
    overallCount=sum(countsVal)
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
    return (contryNames,countsVal,logVals,overallCount,maxVal)

def Compile_LineBardata():
    contryNames,countsVal,logVals,overallCount,maxVal=LineBarData(confirmedGlobal)
    print("\nList of Country.................")
    print(contryNames)

    print("\nList of countsVal.................")
    print(countsVal)

    print("\nList of log of countsVal.................")
    print(logVals)

    print("\noverallCount.................")
    print(overallCount)

    print("\nmaxVal.................")
    print(maxVal)

Compile_LineBardata()
