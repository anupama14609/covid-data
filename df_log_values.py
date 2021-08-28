import pandas as pd 
import numpy as np

def df_log_values(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    countsVal=list(df['values'].values)
    print(countsVal)
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
    print(logVals)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_log_values(dfglobal) 