#file_location = '/Users/danie/OneDrive/NON-PERSONAL/Programming/dnPythonFiles/learningPython/uoft_ltp_1/gradesfile.txt'
gradefile = open('gradesfile.txt.','r')

def read_grades(gradefile):
    # Skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    
    # Read the grades, accumulating them into a dict
    grd_to_ids = {}
    line = gradefile.readline()
    
    while line != '':
        student_id = line[:4]
        grade = float(line[4:].strip())
        
        if grade not in grd_to_ids:
            grd_to_ids[grade] = [student_id] # assign inner element
        else:
            grd_to_ids[grade].append(student_id)
        
        line = gradefile.readline() #read another line
        
    return grd_to_ids
            
print(read_grades(gradefile))
    

