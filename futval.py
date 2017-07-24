# futval.py
#   A program that to compute the value of an investment some time in the future

def main():
    print("This program calculates the future value of a 10 year investment")
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    
    for i in range(10):
        principal = principal * (1 + apr)
        
    print("The value of the investment 10 years from now will be: ", principal)
    
main()