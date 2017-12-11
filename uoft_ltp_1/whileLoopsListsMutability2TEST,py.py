
# not sure how this turns variable values into 3,4,5
def increment_items(L,increment):
	i = 0
	while i < len(L):
		L[i] = L[i] + increment
		i = i + 1
		
values = [1,2,3]
print(values)
print(increment_items(values,2))
print(values)


"""

def while_version(L):
    # (list of number) -> number
    
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1
    return total

"""
