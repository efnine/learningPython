import pandas as pd
import os


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
df.to_excel('new_stocks.xlsx', index=False,startrow=3,startcol=4)

with pd.ExcelWriter('new_stocks.xlsx') as writer:
    df.to_excel(writer, index=False,sheet_name='test_1',startrow=3,startcol=4)
    df.to_excel(writer, index=False,sheet_name='test_2',startrow=2,startcol=2)
    
os.system(r"open -a 'C:\Program Files (x86)\Microsoft Office\root\Office16\Microsoft Excel.app' 'C:\Users\danie\OneDrive\NON-PERSONAL\Education\Programming\dnPythonFiles\learningPython\pandas\new_stocks.xlsx'")

# https://www.youtube.com/watch?v=EaGbS7eWSs0&list=PLeo1K3hjS3uuASpe-1LjfG5f14Bnozjwy&index=5
