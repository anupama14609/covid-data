import pandas as pd 

def df_column_min_value(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    count_list = list(df['values'].values)
    min_value = min(count_list)
    print(min_value)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_column_min_value(dfglobal) 