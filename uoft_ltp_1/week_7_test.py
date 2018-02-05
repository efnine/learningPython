####1 
# d = {'a': 1, 'b': 2}
# CODE MISSING HERE
# {'a': 1, 'c': 3, 'b': 2}
d = {'a': 1, 'b': 2}
# d['c'] = 3
#answer
#d.update({'c':3})
d['c'] = 3
print(d)
print('\n')


###2
# >>> d = {'a': 1, 'b': 2}
# >>> # CODE MISSING HERE
# >>> d
# {'a': 1, 'b': 3}
d = {'a': 1, 'b': 2}
#answer
#d.update({'b':3})
d['b'] = 3
print(d)
print('\n')


###3
# >>> d = {'a': [1, 3], 'b': [5, 7]}
# # CODE MISSING HERE
# >>> d
# {'a': [1, 2, 3], 'b': [5, 7]}
d = {'a': [1, 3], 'b': [5, 7]}
#answer
d['a'].insert(1, 2)

d['a'].append(2)
d['a'].sort()
print(d)
print('\n')


###4
d = {'a': 1, 'c': 3, 'b': 2}
#answer
print("b" in d)

print(not ('e' in d))
print('\n')


###5
d = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}
#answer
print(len(d['a']) + len(d['c']))

print(len(d))

len(d['b'])

print('\n')


###6
tup = (1, 2, 3)
#answer --- error
# print(tup.append(4))
# print(tup[-2] = 4)
print('\n')


###7
#answer - Select the expression(s) that can be used as dictionary keys.
# ['a', 'b']
# try 1
# d = {1: 2, 3: 4}
# try 2
# ['a', 'b']
# ('single',)
# print(d)
print('\n')


###8
d = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
#not the answer 
# total = 0
# for k in d:
#     total = total + len(d[k])
# print(total)
# answer 
total = 0
for k in d:
    total = total + k
print(total)
print('\n')


###9
print({1: 10, 1: 20, 1: 30})
#answer
#{1: 30}
print('\n')


###10
L = [['apple', 3], ['pear', 2], ['banana', 3]]
d = {}
for item in L:
   d[item[0]] = item[1]
print(d)
print('\n')
"""
Populates dictionary d where each key is the first item of 
each inner list of L and each value is the second item of that inner list.
"""

###11
def eat(d):
    '''(dict of {str: int}) -> bool

    Each key in d is a fruit and each value is the quantity of that fruit.

    REST OF DESCRIPTION MISSING HERE

    >>> eat({'apple': 2, 'banana': 3, 'pear': 3, 'peach': 1})
    True
    >>> eat({'apple': 0, 'banana': 0})
    False
    '''
    ate = False
    for fruit in d:
        print(d[fruit])
        print('\n')
        if d[fruit] > 0:
            d[fruit] = d[fruit] - 1
            ate = True

    return ate

print(eat({'apple': 1, 'banana': 2, 'pear': 3, 'peach': 4}))
print('\n')
"""
Try to eat one of each fruit: reduce by 1 all quantities greater 
than 0 associated with each fruit in d and return True 
if and only if any fruit was eaten.
"""

###12
def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    # CODE MISSING HERE -- use both of these
#     for k in d:
#         if v in d[k]:
#             found = True

    for k in d:
        for i in range(len(d[k])):
            if d[k][i] == v:
                found = True
 
    return found

print(contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}))
print(contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}))
