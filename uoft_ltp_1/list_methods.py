def double_even_indices(lst):
    """(list of ints) -> NoneType

    Doubles evey other int in lst, starting at index 0.
    """
    i = 0
    while i < len(lst): # note that lent of lst is 7 and i was set to 0
        lst[i] = lst[i] * 2 # first item on the list is 11 which becomes 22
        i = i + 2 # i is initally 0, then becomes 2, then becomes 4, and 6, and 8, etc...
        
list1 = [11,12,13,14,15,16,17]
print(list1)
double_even_indices(list1)
print(list1)
        

"""
THe example below showcases how type str in immutable as opposed to type list
def interrupted(s):
    s[-1] = "-"
    
greeting = "How are you"
interrupted(greeting)
print(interrupted)
"""

"""
def double_first_element(lst):
    if len(lst) > 0:
        lst[0] = lst[0] * 2

list1 = [10,100,1000]

"""


"""

colors = []
promt = "What's your fav color? "
color = input(promt)
while color != "":
    colors.append(color)
    color = input(promt)

"""
    
