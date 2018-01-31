''' grocery_list = ["Arepa","bananas","tomatos","potatos","toilet paper"]

print("first item is", grocery_list[0])

grocery_list[0] = "Green Juice"

print("first item is", grocery_list[0])

#other list; list within list

other_stuff = ["Wash Car","Pay Bills","Call Garbage Co"]

to_do_list = [other_stuff,grocery_list]

print(to_do_list[1][1])

grocery_list.append("Milkshake")
print(grocery_list)

grocery_list.insert(1,"Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = grocery_list + other_stuff

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

'''

'''
#Tuples -- for when you dont want for data to be easily changed
import random
import sys
import os

pi_tuple(1,3,4,5,4,6,7)

new_tuple = list(pi_tuple)
new_tuple2 = tuple(new_tuple)

'''

'''

#dictionaries

super_villans = {'Fidler': 'Isaac Bowing','Captain Cold': 'Leonard Snart' }

print(super_villans['Captain Cold'])

super_villans['Pied Piper'] = 'Samantha Black'

print(super_villans.get('Pied Piper'))

print(super_villans.keys())

print(super_villans.values())

'''
