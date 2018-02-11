import pandas as pd
import numpy as np

df = pd.read_csv('weather_file3.csv')
### lets replace values
new_df = df.replace({
                    'temperature':['-999999','xxxxxx'],
                    'windspeed':['-999999','xxxxxx'],
                    'event':'No Event'}
                    ,np.NaN)
# DataFrame.replace(
#         to_replace=None,
#         value=None,
#         inplace=False,
#         limit=None,
#         regex=False, 
#         method='pad',
#         axis=None)

print(new_df)
print('\n')

df = pd.read_csv('weather_file4.csv')
### lets replace values
df = df.replace({
                    'temperature':['-999999','xxxxxx'],
                    'windspeed':['-999999','xxxxxx'],
                    'event':'No Event'}
                    ,np.NaN)

new_df = df.replace({
                    'temperature':'[A-za-z]',
                    'windspeed':'[A-Za-z]'}
                    ,'',regex=True)
# DataFrame.replace(
#         to_replace=None,
#         value=None,
#         inplace=False,
#         limit=None,
#         regex=False, 
#         method='pad',
#         axis=None)

print(new_df)