import pandas as pd 
import numpy as np

def df_column_range(dfglobal):
    df_cols_range = dfglobal[dfglobal.columns[4:-1]]
    print(df_cols_range)

    # df_cols_range_vals = dfglobal.columns[4:-1].values
    # print(df_cols_range_vals)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_column_range(dfglobal)
