import pandas as pd
from collections import OrderedDict
from datetime import date

# the "default" manner to create a pandas DF in python is to use a
# list of dictionaries, with each dict key used for the column
# headings.

sales = [{'Account' :'Jones LLC', 'Jan' : 150, 'Feb' : 200, 'Mar' : 140},
         {'Account' : 'Alpha Co.', 'Jan' : 200, 'Feb' : 210, 'Mar' : 215},
         {'Account' : 'Blue Inc', 'Jan' : 50, 'Feb' : 90, 'Mar' : 95}]

df = pd.DataFrame(sales) # defualt list of dict
print("Method 1")
print(df)
print('\n')


# if instead, you would like to design the DF in a "column" oriented way
# use the "from_dict" method.

sales = {'Account' : ['Jones LLC','Alpha Co', 'Blue Inc'],
         'Jan' : [150 , 200, 50],
         'Feb' : [200,210,90],
         'Mar' : [140,215,95]}

df = pd.DataFrame.from_dict(sales) # from_dict
print("Method 2")
print(df)
print('\n')


# the other option is to build the DF data within a list structure
sales = [('Jones LLC', 150, 200, 50),
         ('Alpha Co',200 , 210, 90),
         ('Blue Inc', 140, 215, 95)]
labels = ['Account','Jan','Feb','Mar']
df = pd.DataFrame.from_records(sales, columns=labels) # from_records
print("Method 3")
print(df)
print('\n')

# the other option is to build the DF data within a list structure
sales = [('Account',['Jones LLC', 'Alpha Go','Blue Inc.']),
         ('Jan',[150,200,50]),
         ('Feb',[200,210,90]),
         ('Mar',[140,215,95])]
df = pd.DataFrame.from_items(sales) # from_items
print("Method 4")
print(df)
print('\n')


      



