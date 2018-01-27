# the pizzeria example
def makePizza(number_of_toppings):
    customer_toppings = []
    toppings_count = 0
    for i in range(0,number_of_toppings):
        available_toppings = ['mushrooms','cheese','chicken','pianeapple','bacon']
        costumer_topping = input("Which topping would you like in your pizza? ")
        if costumer_topping in available_toppings:
            toppings_count = toppings_count + 1
            if toppings_count < number_of_toppings:
                print("Perfect! I will add " + costumer_topping.title() + " to your pizza\n")
                customer_toppings.append(costumer_topping)
        else:
            print("Sorry, we do not have " + costumer_topping.title() + " as a featured topping.\n")
                
            
    print("Today we will make a pizza with: " + str(customer_toppings))
    
makePizza(2)


