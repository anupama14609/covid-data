import pandas as pd 
import numpy as np 

covid_confirm_case =pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
unique_country = pd.unique(covid_confirm_case['Country/Region'])
print(unique_country)
