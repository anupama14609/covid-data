import pandas as pd 
import numpy as np

def df_log_values(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    val_list =list(df['values'].values)
    print(val_list)
    print("\n")
    for val in val_list:
        if val!= 0:
            logVals = np.log(val) 
            print(logVals)

        else:
            logVals = 0 

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_log_values(dfglobal) 