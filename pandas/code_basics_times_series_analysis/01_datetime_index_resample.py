import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('aapl.csv',
                 parse_dates=['Date'], # turns dates into datime type
                 index_col='Date' # makes column date the index
                 )
print("\n----------------------------------------")
print(df.head(5))
print("----------------------------------------\n")


### Give me the prices of aapl in Jan
new_df = df['2017-01']
print("\n----------------------------------------")
print(new_df.head(5))
print("----------------------------------------\n")


### What has been the average price of appl during Jan 
new_df = df['2017-01']['Close'].mean()
print("\n----------------------------------------")
print("The mean is: " + str(new_df))
print("----------------------------------------\n")


### What has been the average price of appl during all Janury months available
new_df = df['Close'].resample('W').mean().plot()
#new_df = df['2017-01-07':'2017-01-01']['Close'].mean()
print("\n----------------------------------------")
print(new_df)
plt.show()
print("----------------------------------------\n")