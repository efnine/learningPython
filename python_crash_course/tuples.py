# tuples are immutable. in other words, they
# do not change

dimensions = (200,50)
print(dimensions)

# although tuples are immutable, one could change the 
# variables storing the contents of the TupleSubclass
# for example, we could redefine TupleSubclass
dimensions = (400,100)
