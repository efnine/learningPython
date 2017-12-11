def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1
    return total



"""
# What is the sum of the odd numbers between 1523 and 10504 inclusive?
n = 0
i = 1523

while i < 10504:
    n = n + i
    i = i +2
    if i > 10503:
        print(n)

    # for loop equiv
        >>> n = 0
        >>> for i in range(1523,10504,2):
	n = n + i
	if i > 10502:
		print(n)

"""


#def compress_list(L):
    """(list of str) -> list of str

    return a NEW list with adjacent pairs of string elements from L
    concatanted together, starting with indexes 0 and 1, 2 and 3, etc.

    >>> compress_list(["a","b","c","d"])
    ["ab","cd"]
    """
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list
"""


"""
def secret(s):
    i = 0
    result = ""
    while s[i].isdigit():
         result = result + s[i]
         i = i + 1

    return result
    # Why do ints passed as strings make it puke?
"""
