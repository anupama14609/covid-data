import pandas as pd 
import numpy as np 

confirm_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
confirm_df_country = confirm_df[confirm_df.columns[1]]
confirm_df_date = confirm_df[confirm_df.columns[-1]]

confirm_df_country_date = confirm_df[list(confirm_df.columns[1:2]) + list([confirm_df.columns[-1]])]

print(confirm_df_date)
print(confirm_df_country)
print(confirm_df_country_date )




