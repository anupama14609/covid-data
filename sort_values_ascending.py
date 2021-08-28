import pandas as pd 

def sort_by_values(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    df_unsorted = df 
    print(df_unsorted)

    df_sort_ascending = df.sort_values(by='values', ascending=True)
    print(df_sort_ascending)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
sort_by_values(dfglobal) 