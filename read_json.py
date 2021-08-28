import pandas as pd
import numpy as np

json_df = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
print(json_df)