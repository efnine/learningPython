import pandas as pd


###Lets create 2 dataframes 
india_weather = pd.DataFrame({
                'city':['mumbai','delhi','banglore'],
                'temperature':[32,45,30],
                'humidity':[80,60,78]
                })
print(india_weather)

us_weather = pd.DataFrame({
                'city':['new york','chicago','orlando'],
                'temperature':[21,14,35],
                'humidity':[68,65,75]
                })
print(us_weather)

### now lets concatanate these dfs 
all_weather = pd.concat([india_weather,us_weather],ignore_index=True,keys=['india','us'])
print('-------------------------------------------')
print('Concataned df')
print(all_weather)

### creating keys for the dfs
all_weather = pd.concat([india_weather,us_weather],keys=['india','us'])
print('-------------------------------------------')
print(all_weather)

### once we've estabnlished keys, one can slice by keys
print('-------------------------------------------')
print(all_weather.loc['india'])
print(all_weather.loc['us'])

### what happens when we do not want to concat but append instead?
### lets create two dfs to demonstrate
temperature_df = pd.DataFrame({
                'city':['mumbai','delhi','banglore'],
                'temperature':[32,45,30]
                })
windspeed_df = pd.DataFrame({
                'city':['mumbai','delhi','banglore'],
                'windspeed':[7,12,9]
                })
print('-------------------------------------------')
print(temperature_df)
print(windspeed_df)
print('-------------------------------------------')

### Note that concat sucks because it doesnt merge on key
new_df = pd.concat([temperature_df,windspeed_df],axis=1)
print(new_df)
print('-------------------------------------------')

### It is better to use merge on keys
df1 = pd.DataFrame({
                'city':['mumbai','delhi','banglore'],
                'temperature':[32,45,30]
                })
df2 = pd.DataFrame({
                'city':['mumbai','delhi','banglore'],
                'windspeed':[7,12,9]
                })
new_df = pd.merge(df1,df2,on='city')
print('Merged df')
print(new_df)
print('-------------------------------------------\n')


### What happens if dataset is incomplete
df1 = pd.DataFrame({
                'city':['mumbai','delhi'],
                'temperature':[32,45]
                })
df2 = pd.DataFrame({
                'city':['mumbai','delhi','san francisco','orlando'],
                'windspeed':[7,12,9, 13]
                })
new_df = pd.merge(df1,df2,on='city',how='outer',indicator=True) # outer is also known as 'junion'
print('Outer merged df')
print(new_df)
print('-------------------------------------------\n')


### Whats happens if dataset has data for two exact columns
df1 = pd.DataFrame({
                'city':['mumbai','delhi'],
                'temperature':[32,45]
                })
df2 = pd.DataFrame({
                'city':['mumbai','delhi'],
                'temperature':[32,45]
                })
new_df = pd.merge(df1,df2,on='city',
                  how='outer',
                  indicator=True, 
                  suffixes=('_left','_right'))
print('duplicate Fields merged df')
print(new_df)
print('-------------------------------------------\n')









































