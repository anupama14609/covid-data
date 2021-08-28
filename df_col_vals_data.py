import pandas as pd 

def df_column_values_data(dfglobal):
    df = dfglobal[list(dfglobal.columns[1:2]) + list([dfglobal.columns[-1]])]
    df.columns = ['Country/Region','values']

    country_list = list(df['Country/Region'].values)
    print(country_list)
    
    count_list = list(df['values'].values)
    print(count_list)

dfglobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
df_column_values_data(dfglobal) 