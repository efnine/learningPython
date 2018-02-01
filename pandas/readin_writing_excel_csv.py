import pandas as pd

def convert_dvd_yld(cell):
    if cell == 'n.a.':
        return 'HIHIHIHI'

df = pd.read_csv('stocks.csv',header=None, skiprows=1, 
                 names = ['BAR_DATE','BBG_TICKER','NAME','PRICE','DVD_YIELD'],
                 na_values = {'DVD_TYPE' : 'n.a' ,
                 'PRICE' : -1},
                 converters = {'DVD_YIELD':convert_dvd_yld}) # specifying dict
print(df)



df.to_csv('new_stocks.csv', index=False)

#https://www.youtube.com/watch?v=-0NwrcZOKhQ&list=WL&index=4&t=1s
# at the 19 minute mark
