import pandas as pd 
import numpy as np 

covid_confirm_case =pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
country_list = pd.unique(covid_confirm_case['Country/Region']).tolist()
print(country_list)
