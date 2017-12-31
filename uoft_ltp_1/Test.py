import pandas as pd
import matplotlib

#Q1
"""
def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

[6, 15, 24]
"""

#Q2
"""
def mystery(s):
    #(str) -> bool
    
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is this line reached? = 2
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')

two times
 
"""


#Q3 
"""
def mystery(s):

    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)

print(mystery("BB"))
#xxxxReturn True if and only if there are exactly len(s) // 2 
#xxxxcharacters in s that are the same character.

#xxxReturn True if and only if s[:len(s) // 2]  is the same as s[len(s) // 2:].

#this is the one
Return True if and only if s is equal to the reverse of s.

"""

#Q4
L = ["A","B","C","D"]

def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the 
    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE
    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
        
    L[0] = last_item
    
    return L

print(shift_right(L))


#5
def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with 
    the string from the corresponding position of list1 and the
    int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    # CODE MISSING HERE
    #for i in range(len(list1)):
        #pairs.append([list1[i], list2[i]])
        
    #for i in range(len(list1)):
        #inner_list = []
        #inner_list.append(list1[i])
        #inner_list.append(list2[i])
        #pairs.append(inner_list)
        
    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))


#6
#values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#values[1][1]


#7
>>> treats = [['apple', 'pie'], ['vanilla', 'ice-cream'], ['chocolate', 'cake']]
>>> treats[-3][-1]

>>> breakfast = [['French', 'toast'], ['blueberry', 'pancakes'], ['scrambled', 'eggs']]
>>> breakfast[-2][-2]
'blueberry'


#8 xxxx
"""
for i in range(2, 5): #this loops 3 times
    for j in range(4, 9): #this loops 5 times
        print(i, j) # therefore, this loops 3 * 5 = 15 times
        
        trying 5 times now?
        
        try 3 times?
        
        trying 24?
        
"""

#9
def contains(value, lst):
    # We have not yet found value in the list.
    found = False
    
    # CODE MISSING HERE
    #for sublist in lst:
        #if value in sublist:
            #found = True
            
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
            
    return found
print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],[80, 100]]))


#10
"""
A file has a section at the top that has a preamble describing the 
contents of the file, then a blank line, then a list of high 
temperatures for each day in January all on one line, then a list of 
high temperatures for each day in February all on one line, then lists 
for March, April, and so on through December, each on one line. There 
are thousands of lines of information after that temperature data that 
you aren't currently interested in.

You want to write a program that prints the average of the high 
temperatures in January. Which of the four file-reading approaches 
should you use?

Hint: review the Reading Files lecture.

the READLINE approach
"""

#11 xxxx
"""
for line in data_file:
     print(line)

The program above prints the lines of the file but adds an extra blank
line after each line. Select the code fragment(s) that when used as 
replacement(s) for print(line) will print the lines without extra
blank lines.

print(line.rstrip('\n')) + print(line, end='') xxxxx

print(line.rstrip('\n')) + print(line.strip()) xxxxx

print(line, end='') + print(line.strip()) xxxxx

print(line.rstrip('\n')) + pprint(line - '\n')


"""


#12
print("\nQ.12")
def lines_startswith(file, letter):
     """ (file open for reading, str) -> list of str

     Return the list of lines from file that begin with letter.     
     The lines should have the newline removed.

     Precondition: len(letter) == 1
     """

     matches = []

     # CODE MISSING HERE            
    for line in file:
        if line.startswith(letter):
            matches.append(line.rstrip('\n'))
    + 
    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
            
            
#13

def write_to_file(file, sentences):
    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.
    """

    # CODE MISSING HERE
       for s in sentences:
        file.write(s)
        file.write('\n')
        
        for s in sentences:
        file.write(s + '\n')
    
            
     return matches

print()

"""
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
print(pen(path).readline())


#words = ["HELLO","WORLD"]
words = ['EFJAJCOWSS\n', 'SDGKSRFDFF\n', 'ASRJDUSKLK\n', 'HEANDNDJWA\n', 'ANSDNCNEOP\n', 'PMSNFHHEJE\n', 'JEPQLYNXDL']

# First we have to clean the list of the "\n"
new_words_list = []
for i in range(len(words)):
    cleaned_words = words[i].strip("\n")
    new_words_list.append(cleaned_words)
    #return new_words_list

# Second we have to turn each char within each list element into a str
# Each list element must have its own line
char_list = []
for i in range(len(new_words_list)): # for every element in words -> 2
    subject_word = new_words_list[i] # store the value of each word
    my_list = []
    for i in range(len(subject_word)): # for every element in each word -> 5
        my_list.append(str(subject_word[i])) # give me a list with each char
        #print(my_list)
    char_list.insert(i,my_list)
print(char_list[0])
        
        
#print(char_list)

"""