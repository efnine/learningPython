#Pg 47
cars = ["bmw", "audit","toyota","subaru"]
cars.sort() # when a method is used on a list, the list is permanently modified
print(cars)

cars = ["bmw", "audit","toyota","subaru"] # need to redefine list
cars.sort(reverse=True) # when a method is used on a list, the list is permanently modified
print("\n")
print(cars)

#to not alter the order of a list use the sorted method
cars = ["bmw", "audit","toyota","subaru"] # need to redefine list
print("\nHere is the original list: \n" + str(cars))
cars_sorted = sorted(cars)
print("\nHere is the sorted list: \n" + str(cars_sorted))
print("\nHere is the original list gain: \n" + str(cars))

cars = ["bmw", "audit","toyota","subaru"] # need to redefine list
print("\n")
print(cars)
cars.reverse() # Once gain, methods wihtin lists modifies them permanently 
print(cars)
