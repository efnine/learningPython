# the pizzeria example
def makePizza(number_of_toppings):
    customer_toppings = []
    toppings_count = 0
    available_toppings = ['mushrooms','cheese','chicken','pianeapple','bacon']
    
    # sometimes a while loop is better than a for loop
    while toppings_count < number_of_toppings:
        costumer_topping = input("Which topping would you like in your pizza? ")
        
        if costumer_topping in available_toppings:
            print("Perfect! I will add " + costumer_topping.title() + " to your pizza\n")
            customer_toppings.append(costumer_topping)
            toppings_count = toppings_count + 1
        else:
            print("Sorry, we do not have " + costumer_topping.title() + " as a featured topping.\n")
    
    print("\nToday we will make a pizza with: " + str(customer_toppings))
    
    
makePizza(2)


