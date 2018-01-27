cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
         
print('\n')
age_o = 22
age_1 = 18
print(age_o >= 21 or age_1 >= 21)

# lets check if a submission has already been submitted
print('\n')
requested_topping = ['mushroom','onions','pinapple']
print('mushroom' in requested_topping)

# lets perform the same check, but this time lets check if the value is not in
# the list
print('\n')
banned_uers = ['joe','dan','manuel']
user = 'mary'
if user not in banned_uers:
    print(user.title() + ", you can post a response if you wish")
    
# booleam expressions
print('\n')
game_active = True
can_edit = False


# types of if statements 
# simple if statements 
if 18 > 5:
    print("yes") 

# if + else 
if 19 > 5:
    print("yes")
else:
    print("nope")

# if + elif
print('\n') 
age = 18
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission price is $" + str(price) + ".")





