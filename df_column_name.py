import pandas as pd 
import numpy as np

def df_columns_name(dfglobal):
    df_cols_name = dfglobal.columns.values
    print(df_cols_name)

    df_cols_values = dfglobal[dfglobal.columns.values]
    print(df_cols_values)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_columns_name(dfglobal)
