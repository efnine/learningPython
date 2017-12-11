"""
file_location = '/Users/danie/AppData/Local/Programs/Python/Python36-32/Flanders Fields.txt'
opened_file = open(file_location,"r")
#line = opened_file.readline()
line = opened_file.read() #reads the entire file into memory at once
print(line)

# use this approach when parsing through specific sections of a file
while line != "\n":
    print(line, end="")
    line = opened_file.readline()

# use this approach when the objective is to read/output all contents in file
for line in opened_file:
    print(line,end="")
"""

"""
file_location = '/Users/danie/AppData/Local/Programs/Python/Python36-32/cat.txt'
opened_file = open(file_location,"r")
line = opened_file.read() #reads the entire file into memory at once
print(line[3])
"""

file_location = '/Users/danie/AppData/Local/Programs/Python/Python36-32/students.txt'
opened_file = open(file_location,"r")
lines = opened_file.readlines() #reads the entire file into memory a
lines.sort()
