s1 = "banana"
s2 = "ana"
s1.find(s2,5)


"""
digits = "0123456789"
result = 0
for digit in digits:
    result = digit
print(result)
"""

def common_chars(s1, s2):

    res = ""
    for ch in s1:
        if ch in s2:
            res = res + ch
    return res
            

"""
message = "Happy 29th!"
new_msg = ""

for char in message:
    if not char.isdigit():
        new_msg = new_msg + char
        #new_msg = new_msg + str((int(char)+1) % 10)
    else:
        new_msg = new_msg + str((int(char)+1) % 10)
        #new_msg = new_msg + char      

print(new_msg)
"""


def count_vowels(s):
    """(str) -> int

    returns the number of vowels within a specified string

    >>> count_vowels("Happy Anniversary!")
    5
    >>> count_vowels("xyz")
    0
    """

    count_vowels = 0

    for char in s:
        if char in "aeiouAEIOU":
            count_vowels = count_vowels + 1
    return count_vowels 


def collect_vowels(s):
    """(str) -> int

    returns the vowels within a specified string

    >>> collect_vowels("Happy Anniversary!")
    "aAiea"
    >>> collect_vowels("xyz")
    ""
    """

    collect_vowels = ""

    for char in s:
        if char in "aeiouAEIOU":
            collect_vowels = collect_vowels + char
    return collect_vowels 
