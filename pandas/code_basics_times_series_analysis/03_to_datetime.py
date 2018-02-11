import pandas as pd

dates = ['2017-01-05', 'Jan 5,2017', '01/05/2017', '2017.01.05',
         '2017/01/05', '20170105']
new_dates = pd.to_datetime(dates)
print("\n----------------------------------------")
print(new_dates)
print("----------------------------------------\n")


eur_date = pd.to_datetime('5/1/2017') # europe dd/mm/yyyy
us_date = pd.to_datetime('5/1/2017') # us mm/dd/yyyy
eur_to_us_date = pd.to_datetime('5/1/2017', dayfirst=True) # europe dd/mm/yyyy
custom_date = pd.to_datetime('5$1$2017', format='%d$%m$%Y') # custom
print("\n----------------------------------------")
print(eur_date)
print(us_date)
print(eur_to_us_date)
print(custom_date)
print("----------------------------------------\n")
