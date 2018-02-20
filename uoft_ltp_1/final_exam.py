### 1 ###
# Select the expression(s) that evaluate to a float value.
# 
# 
# 3 / 4
# 
# 7 + 8.5
# 
# 8 % 6
# 
# 3 // 4



### 2 ###
# a = 7
# b = a + 3
# a = 9
# After the code above has been executed, what value does b refer to?
# 10


### 3 ###
# def f(y):
#     x = y * 3
#     return y + x
# 
# print(f(10)) # 40


### 4 ###
# start = 'L'
# middle = 8
# end = 'R'
# 
# print(start+str(middle)+end)

# first = 'pwn'
# second = 3
# third = 'd'
# msg = first+str(second)+third
# print(msg)


### 5 ###
# def smaller_of_largest(L1, L2):
#     '''(list of int, list of int) -> int
#  
#     Return the smaller of the largest value in L1 and the 
#     largest value inL2.
#  
#     Precondition: L1 and L2 are not empty.
#  
#     >>> smaller_of_largest([1, 4, 0], [3, 2])
#     3
#     >>> smaller_of_largest([4], [9, 6, 3])
#     4
#     '''
#  
#     return min(max(L1),max(L2))
# 
# msg1 = smaller_of_largest([1, 4, 0], [3, 2])
# msg2 = smaller_of_largest([4], [9, 6, 3])
#   
# print(msg1)
# print(msg2)



### 6 ###
# def both_start_with(s1, s2, prefix):
#     '''(str, str, str) -> bool
#  
#     Return True if and only if s1 and s2 both start with the
#     letters in prefix.
#  
#     '''
#     return s1.startswith(prefix) and s2.startswith(prefix)
#      
# #     if s1.startswith(prefix) and s2.startswith(prefix):
# #         return True
# #     else:
# #         return False
#  
# print(both_start_with('sun', 'susan', 's'))


# def same_length(L1, L2):
#     '''(list, list) -> bool
# 
#     Return True if and only if L1 and L2 contain the same number of elements.
#     '''
#     
# #     if len(L1) == len(L2):
# #        return True
# #     else:
# #        return False
# 
#     return len(L1) == len(L2)


### 7 ###
# def burble(a, b):
#     '''(int, float) -> str'''
#     print(a)
#     print(b)
#   
# 
# def snorgle(L):
#     '''(list of str) -> float
#     Precondition: L has at least one element.'''
#     print(L)
#     
# # print(burble(len(burble(1, 2.2)), 3.3)) # nope
# # print(burble([snorgle(1, 1.0), 'b'])) # nope
# # print(burble(8 // 3, snorgle(['a', 'b', 'c']))) # yes
# print(burble(burble(1, 1.0), 'b')) # yes




### 8 ###
# def reverse(s):
#     '''(str) -> str
# 
#      Return the reverse of s.
# 
#      >>> reverse('abc')
#     'cba'
#     >>> reverse('a')
#     'a'
#     >>> reverse('madam')
#     'madam'
#     >>> reverse('1234!')
#     '!4321'
#     '''
#     result = ''
#     i = len(s) - 1
#     while i >= 0:
#         result = result + s[i]
#         i = i - 1 
#     return result
# 
# print(reverse('abc'))


# def gather_every_nth(L, n):
#     '''(list, int) -> list
# 
#     Return a new list containing every n'th element in L, 
#     starting at index 0.
# 
#     Precondition: n >= 1
# 
#     >>> gather_every_nth([0, 1, 2, 3, 4, 5], 3)
# 
#     [0, 3]
#     >>> gather_every_nth(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 2)
#    ['a', 'c', 'e', 'g', 'i']
#    '''
#     result = []
#     i = 0
#     while i < len(L):
#         result.append(L[i])
#         i = i + n
#    
#     return result# 
# msg = gather_every_nth([0, 1, 2, 3, 4, 5], 3)
# print(msg)


### 9 ###
# def get_keys(L, d):
#     '''(list, dict) -> list
# 
#     Return a new list containing all the items in L that are keys in d.
# 
#     >>> get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'})
#     [1, 'a']
#     '''
#   
#     result = []
#     for k in d: # CODE MISSING HERE
#        if k in L:
#           result.append(k) 
# 
#     return result
#  
# print(get_keys([1, 2, 'a'], {'a': 3, 1: 2, 4: 'w'}))




### 10 ###
# def count_values_that_are_keys(d):
#     '''(dict) -> int
# 
#     Return the number of values in d that are also keys in d.
#    
#     >>> count_values_that_are_keys(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
#     3
#     >>> count_values_that_are_keys({1: 1})
#     1
#     >>> count_values_that_are_keys({1: 2, 2: 3, 3: 0})
#     2
#     >>> count_values_that_are_keys({1: 2})
#     0
#     '''
# 
#     result = 0
#     for k in d:
#         if d[k] in d: # CODE MISSING HERE
#              result = result + 1
# 
#     return result
# 
# print(count_values_that_are_keys({1: 2, 2: 3, 3: 3}))
# print(count_values_that_are_keys({1: 1}))
# print(count_values_that_are_keys({1: 2, 2: 3, 3: 0}))
# print(count_values_that_are_keys({1: 2}))


### 11 ###
# def double_values(collection):
#     for v in range(len(collection)):
#          collection[v] = collection[v] * 2
         
# def double_last_value(L):
#     '''(list of int) -> NoneType
# 
#     Double the value at L[-1]. For example, if L[-1] is 3,
#     replace it with 6.
# 
#     Precondition: len(L) >= 1.
#     '''
# L1 = [1, 3, 5]
# double_last_value(L1)
# print(L1[-1]) --> 10


### 12 ###
# def get_diagonal_and_non_diagonal(L):
#     '''(list of list of int) -> tuple of (list of int, list of int)
# 
#     Return a tuple where the first item is a list of the values on the
#     diagonal of square nested list L and the second item is a list of the rest
#     of the values in L.
# 
#     >>> get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]])
#     ([1, 4, 8], [3, 5, 2, 5, 4, 0])
#     '''
# 
#     diagonal = []
#     non_diagonal = []
#     for row in range(len(L)):
#         for col in range(len(L)):
#             
#             # yes
# #             if row == col:
# #                 diagonal.append(L[row][col])
# #             elif row != col:
# #                 non_diagonal.append(L[row][col])
#             
#             # yes
# #             if row == col:
# #                 diagonal.append(L[row][row])
# #             else:
# #                 non_diagonal.append(L[row][col])
# 
#             # yes
# #             if row == col:
# #                 diagonal.append(L[row][col])
# #             else:
# #                 non_diagonal.append(L[row][col])
# 
#             # yes
# #             if row == col:
# #                 diagonal.append(L[row][col])
# #             if row != col:
# #                 non_diagonal.append(L[row][col])
#                 
#             #No
#             if row == col:
#                 diagonal.append(L[row][col])
# 
#             non_diagonal.append(L[row][col])
#             
# 
#     return (diagonal, non_diagonal)
# 
# 
# print(get_diagonal_and_non_diagonal([[1,  3,  5], [2,  4,  5], [4,  0,  8]]))



### 13 ###
# def add_to_letter_counts(d, s):
#     '''(dict of {str: int}, str) -> NoneType
# 
#     d is a dictionary where the keys are single-letter strings
#     and the values are counts.
# 
#     For each letter in s, add to that letter's count in d.
# 
#     Precondition: all the letters in s are keys in d.
# 
#     >>> letter_counts = {'i': 0, 'r': 5, 'e': 1}
#     >>> add_to_letter_counts(letter_counts, 'eerie')
#     >>> letter_counts
#     {'i': 1, 'r': 6, 'e': 4}
#     '''
# 
#     for c in s:
#         d[c] = d[c] + 1 # CODE MISSING HERE
# 
# 
# letter_counts = {'i': 0, 'r': 5, 'e': 1}
# add_to_letter_counts(letter_counts, 'eerie')
# print(letter_counts)


# def count_chars(s):
#     '''(str) -> dict of {str: int}
# 
#     Return a dictionary where the keys are the characters in s 
#     and the values are how many times those characters appear in s.
# 
#     >>> count_chars('abracadabra')
#     {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
#     '''
#     d = {}
# 
#     for c in s:
#         if not (c in d):
#             d[c] = 1
#         else:
#             d[c] = d[c] + 1
# 
#     return d
# 
# 
# print(count_chars('abracadabra'))
















