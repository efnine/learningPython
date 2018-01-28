# the pizzeria example
def makePizza(number_of_toppings):
    customer_toppings = []
    toppings_count = 0
    pizza_price = 10
    toppings_w_prices = {'mushrooms':4,'cheese':1,'chicken':5,'pineaaple':2,'bacon':3}
    
    # sometimes a while loop is better than a for loop
    while toppings_count < number_of_toppings:
        costumer_topping = input("Which topping would you like in your pizza? ")
        
        if costumer_topping in toppings_w_prices:
            print("Perfect! I will add " + costumer_topping.title() + " to your pizza\n")
            customer_toppings.append(costumer_topping)
            toppings_count = toppings_count + 1
            pizza_price = pizza_price + toppings_w_prices[costumer_topping]
        else:
            print("Sorry, we do not have " + costumer_topping.title() + " as a featured topping.\n")
    
    print("\nToday we will make a pizza with: " + str(customer_toppings))
    print("Your pizza will cost $" + str(pizza_price))
    
    
makePizza(2)


