### list comprehension ####
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
print(out)
print("Let me show you the output of a list comprehension:")
print([num**2 for num in x])


### lambda expressions ###
def times2(num):
    return num*2
   
seq = [1,2,3,4,5]
print('\nBelow is a map:')
print(list(map(times2,seq)))


# lets write the lambda expression
my_lambda = lambda num: num*2 # note how the 'num' is used
print('\nBelow is a lambda expression:')
print(my_lambda(2))
print('\nBelow is a map with a lambda expression:')
print(list(map(my_lambda,seq)))


### filter function ###
my_filter = filter(lambda num: num%2 == 0, seq)
print('\nBelow is a filter with a lambda expression:')
print(list(my_filter))


### split method ###
tweet = "Go Sports! # Sports"
print("\nBelow is the split method used to remove the hashtag "
      "element from a tweet:")
print(tweet.split('#')[1])


### tuple unpacking ###
t = [(1,2),(3,4),(5,6)]
for a,b in t:
    print(a)
    print(b)