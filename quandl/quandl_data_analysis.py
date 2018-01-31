import quandl
import pandas as pd

mydata = quandl.get('WIKI/GS')

#mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')

#mydata = quandl.get('NSE/OIL')

#mydata.to_csv('out.csv')

print (mydata.tail())