even_numbers = list(range(2,11,2))
#print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# lets write the above in a more pythonic way
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)


# lets write the above in an even more pythonic way
squares = [value**2 for value in range(1,11)] # this is called a list comprehension
print(squares)

# a few python funtions are are specific to
# list of numbers. For example, you can easily
# find the min, max, and sum of a list of numbers.

print(min(squares))
print(max(squares))
print(sum(squares))


"""
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list


Built-in Functions with List
Function    Description
all()    Return True if all elements of the list are true (or if the list is empty).
any()    Return True if any element of the list is true. If the list is empty, return False.
enumerate()    Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()    Return the length (the number of items) in the list.
list()    Convert an iterable (tuple, string, set, dictionary) to a list.
max()    Return the largest item in the list.
min()    Return the smallest item in the list
sorted()    Return a new sorted list (does not sort the list itself).
sum()    Return the sum of all elements in the list.

"""