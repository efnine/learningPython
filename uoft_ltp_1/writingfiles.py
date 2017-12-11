"""
#opening and saving files via tkinter
import tkinter.filedialog
from_filenmae = tkinter.filedialog.askopenfilename()
to_filenmae = tkinter.filedialog.asksaveasfilename()
"""

from_file = open("cat.txt","r")
contents = from_file.read()

to_file = open("cat-copy.txt","w")
to_file.write("Copy\n\n")
to_file.write(contents)
to_file.close()

print("File was writte!n")






"""
# how to read a file
#file_path = "/Users/danie/AppData/Local/Programs/Python/Python36-32/cat.txt"
file = open("cat.txt","r")
print(file.read())
"""
