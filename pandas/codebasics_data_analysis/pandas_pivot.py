import pandas as pd

df = pd.read_csv('weather_file5.csv')
print("Original df")
print(df)
print("------------------------------------------------\n")


df2 = df.pivot(index='date',columns='city')
print("df2")
print(df2)
print("------------------------------------------------\n")


df3 = df.pivot(index='date',columns='city',values='humidity')
print("df3")
print(df3)
print("------------------------------------------------\n")

df4= pd.read_csv('weather_file6.csv')
print(df4)
print("------------------------------------------------\n")
pivot_df4 = df4.pivot_table(index='city',columns='date',aggfunc='mean')
print("df4")
print(pivot_df4)
print("------------------------------------------------\n")

df5= pd.read_csv('weather_file7.csv')
# lets transfor date from string to datetime type
df5['date'] = pd.to_datetime(df5['date'])
print(df5)
print("------------------------------------------------\n")
pivot_df5 = df5.pivot_table(
                            index=pd.Grouper(freq='M',key='date'),
                            columns='city'
                            ) # grouper M provides end of month
print("df5")
print(pivot_df5)
print("------------------------------------------------\n")