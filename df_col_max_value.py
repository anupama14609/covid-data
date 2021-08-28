import pandas as pd 

def df_column_max_value(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    count_list = list(df['values'].values)
    max_value = max(count_list)
    print(max_value)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_column_max_value(dfglobal) 