import pandas as pd

df = pd.read_csv('weather_file2.csv',parse_dates=['day'])
print(type(df['day'][0]))
df.set_index('day', inplace=True) 
#### inplace parameter must be passed in order 
# to change the dataframe
# print(type(df.day[0]))
print(df)
print('-------------------------------------')

#### make ALL na's 0
# new_df = df.fillna(0)
# print(new_df.head(2))
# print('-------------------------------------')

#### change na's by column
# new_df = df.fillna({
#                     'Temperature':0,
#                     'Events': 'No Event'})
# print(new_df.head(2))
# print('-------------------------------------')

### sometimes we want to fill forward or back
# new_df = df.fillna(method='ffill') # bfill is also used for back fill 
# print(new_df)
# print('-------------------------------------')

### sometime we dont want to fill foward or back --- we want to
### average the missing points
new_df = df.interpolate(method='time')
print(new_df)

### one could drop all the columns with at least 1 na --> df.dropna()
### one could drop all the columns with all rows as na --> df.dropna(how='all')
### one could keep all the columns with n number of nas --> df.dropna(thresh=2)
