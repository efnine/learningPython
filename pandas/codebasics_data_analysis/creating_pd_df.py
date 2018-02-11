import pandas as pd

# 1st way to creating dataframe = read from csv or xls
df = pd.read_csv('weather_file.csv') #read_excel('filename.xlsm','sheet_name')
print(df)
print('\n')

# 2nd way = create a df from a python dict
weather_data = {'date' : ['1/1/2017', '3/1/2017','6/1/2017'],
                'temp' : [-10, 5, 25],
                'windspeed': [6, 5, 4],
                'event' : ['rain', 'sun', 'snow']}
df = pd.DataFrame(weather_data)
print(df)
print('\n')

# 3rd way = create a df from a python tuple. Note that it sorts columns alphabetically
weather_data = [
    ('1/1/2017', -10, 6, 'rain'),
    ('3/1/2017', 5, 5, 'sun'),
    ('6/1/2017', 25, 4, 'snow'),  
    ]

df = pd.DataFrame(weather_data, columns = ['date', 'temp' , 'windspeed' , 'event'])
print(df)
print('\n')

# 4th way = create a pandas df from list of dicts...fuck that
my_dicts = [{'points': 50, 'time': '5:00', 'year': 2010}, 
            {'points': 25, 'time': '6:00', 'month': "february"}, 
            {'points':90, 'time': '9:00', 'month': 'january'}, 
            {'points_h1':20, 'month': 'june'}]
df = pd.DataFrame(my_dicts)
print(df)
print('\n')

my_dicts = [{'points': 50, 'time': '5:00', 'year': 2010}, 
            {'points': 25, 'time': '6:00', 'month': "february"}, 
            {'points':90, 'time': '9:00', 'month': 'january'}, 
            {'points_h1':20, 'month': 'june'}]
df = pd.DataFrame.from_dict(my_dicts)
print(df)
print('\n')

# note that there are even more ways to do this but these should suffice

