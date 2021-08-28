import pandas as pd 
import numpy as np

def df_columns(dfglobal):
    df_cols_last_with_range = dfglobal[dfglobal.columns[1:]]
    print(df_cols_last_with_range)

    df_cols_last_with_norange = dfglobal[dfglobal.columns]
    print(df_cols_last_with_norange)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_columns(dfglobal)
