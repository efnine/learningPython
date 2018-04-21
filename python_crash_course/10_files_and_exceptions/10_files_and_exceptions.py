"""
The keyword 'with' below closes the file once access to it is no longer needed.
Notice how we call open() in this program but not close(). 
You could open and close the file by calling open() and close(), but 
if a bug in your program prevents the close() statement from being executed, 
the file may never
close.
"""
# #---- Example 1
# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
    
    
# #---- Example 2
# with open('pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.rstrip())
        
# #---- Example 3
# with open('pi_digits.txt') as file_object:
#     lines = file_object.readlines()
#     
# for line in lines:
#     print(line.rstrip())
    
# #---- Example 4
# with open('pi_digits.txt') as file_object:
#     lines = file_object.readlines()
#     
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#     
# print(float(pi_string))
# print(len(pi_string))


# #---- Example 5
# with open('pi_million_digits.txt') as file_object:
#     lines = file_object.readlines()
#     
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
    
    
#---- Example 6 [is my bday within pi?]
with open('pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
bday = input("Input your birthday in the folowing format (mmddyyy): ")
if bday in pi_string:
    print("\nYour birthday appears in the first million digits of pi!")
else:
    print("\nYour birthday does not appear in the first million digits of pi :(")
    



















