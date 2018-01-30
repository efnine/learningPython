import pandas as pd


df = pd.read_csv('nyc_weather.csv')
print(df['Temperature'].max())
print('\n')
print(df['EST'][df['Events'] == 'Rain'])
print('\n')
df.fillna(0,inplace=True) # fill the nulls with an int or float
print(df['WindSpeedMPH'].mean())

print("\n*******************************************\n")

df = pd.read_csv('weather_file.csv')
print(df.shape) # out should be read as (rows,columns)
rows , columns = df.shape
print("# of Rows: " + str(rows))
print("# of Columns: " + str(columns))
print('\n')
print(df.head(2))
print(df.tail(2))
print('\n')
print(df[2:5])
print('\n')
print(df.columns)
print('\n')
print(df.day[2:5]) # these are equivalents print(df['day'][2:5])
print('\n')
print(df[['day','event']][2:5]) # accessing only certain columns and certain rows
print('\n')
print(df['temperature'].max())
print('\n')
print(df.describe())
print('\n')
print([df[df['temperature'] >= 32]])
print('\n')
print(df[df['temperature'] == df['temperature'].max()])
print('\n')
print(df[['day','temperature']][df['temperature'] == df['temperature'].max()]) # show me the date and temperature recorded on the hotttest (max) day
print('\n')
df.set_index('day', inplace = True) #inplace = True ensures the df is changed
print(df.loc['1/5/2017'])





print(type(df['event']))
