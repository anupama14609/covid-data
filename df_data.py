import pandas as pd 

def df_data():
    df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    print(df)

    column_name=df.columns
    print(column_name)
    
    country_data = df['Country/Region']
    print(country_data)

    country_list = df['Country/Region'].tolist()
    print(country_list)

df_data() 