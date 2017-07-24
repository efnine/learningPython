# quadratic.py
#   A program that computes the real roots of a quadratic equation
#   The program also illustrates the use of Python's math library
# NOTE: The program crashes if the equation has no real roots

import math #this command makes the math library(module) available 

def main():
    print("This program finds the real solutions to a quadratic equation")
    print()
    
    a,b,c = eval(input("Please enter the coefficients (a,b,c): "))
    
    discRoot = math.sqrt(b*b-4*a*c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)
    
    print()
    print("The solutions are: ", root1, root2)

main()

