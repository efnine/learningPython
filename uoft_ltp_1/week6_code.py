file_location = "/Users/danie/AppData/Local/Programs/Python/Python36-32/Flanders Fields.txt"
file = open(file_location, "r")

def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

    Precondition: len(letter) == 1
    """
    matches = []

    for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))
            
    return matches

print(lines_startswith(file, "W"))
