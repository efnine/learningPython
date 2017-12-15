import pandas as pd
import matplotlib

#print("hello world!")

"""
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
print(pen(path).readline())
"""

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

