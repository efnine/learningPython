def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False

    for sublist in lst:
        if value in sublist:
            found = True

    return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))

+

def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
    return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'], [80, 100]]))




#def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    #pairs = []

    #for i in range(len(list1)):
        #pairs.append([list1[i], list2[i]])

    #return pairs


        for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
make_pairs(['A', 'B', 'C'], [1, 2, 3])




""""
def shift_right(L):
    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]
        
    L[0] = last_item

mylist = ["A","B","C","D"]
shift_right(mylist)
print(mylist)
"""


"""
def mystery(s):

    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)
"""

"""
def mystery(s):
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')
"""


"""
def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
