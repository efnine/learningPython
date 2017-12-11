motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
print("\n")
motorbikes[0]="ducati"
print(motorbikes)
print("\n")

motorbikes = ["honda","yamaha","susuki"]
motorbikes.append("ducati")
print(motorbikes)
print("\n")

motorbikes = ["honda","yamaha","susuki"]
motorbikes.insert(2,"bwm")
print(motorbikes)
print("\n")

motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
del motorbikes[0] # using the del function = no access to elements
print(motorbikes)
print("\n")

motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
popped_motorbike = motorbikes.pop() # the pop method stores the removed element
print(motorbikes)
print(popped_motorbike)
print("\n")

motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
last_owned = motorbikes.pop() # the pop method stores the removed element
print("The last motorbike I owned was a " + last_owned.title() + ".")
print("\n")

motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
first_owned = motorbikes.pop(0) # the pop method stores the removed element
print("The first motorbike I owned was a " + first_owned.title() + ".")
print("\n")

# But what happens when you dont know the index to remove
motorbikes = ["honda","yamaha","susuki"]
print(motorbikes)
motorbikes.remove("yamaha")
print(motorbikes)
print("\n")



