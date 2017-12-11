import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    # lets try to be a little more specific about the headers
    for index, column_header in enumerate(header_row):
        print(index, column_header)

