import csv

with open("out.csv") as csvfile:
    readCSV = csv.reader(csvfile,delimiter=",")
    for row in readCSV:
        print(row[1])
    
    