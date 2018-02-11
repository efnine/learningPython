import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay
from calendar import calendar

df = pd.read_csv('aapl.csv',
                 parse_dates=['Date'],
                 index_col='Date' # makes column date the index
                 )
print("\n----------------------------------------")
print(df.head(5))
print("----------------------------------------\n")

df = pd.read_csv('aapl_no_dates.csv')
print("\n----------------------------------------")
print(df.head(5))
print("----------------------------------------\n")

### because businessdays do not account for jurisdiction specific
### holdiays, one must create or make reference to custom holidays
us_bdays = CustomBusinessDay(calendar=USFederalHolidayCalendar()) 


### lets create a date range from nothing
rng = pd.bdate_range(end='07/07/2017',
                    periods=df.shape[0],
                    freq=us_bdays # 'B'only excludes wekkends
                    )
print("\n----------------------------------------")
print(rng)
print("----------------------------------------\n")


### lets apply the date range we created to the initial df
# TO DO: How to apply the date range to the end of the df?
df.set_index(rng, inplace=True)
print("\n----------------------------------------")
print(df.head(5))
print("----------------------------------------\n")


ts = pd.Series(np.random.randint(1,10,df.shape[0]), index=rng)
print("\n----------------------------------------")
print(ts.head(5))
print("----------------------------------------\n")

