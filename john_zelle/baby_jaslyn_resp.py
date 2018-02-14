# baby_jaslyn.py
#   A program that to compute the value of an RESP investment assuming one deposits some amount every eyar

def main():
    print("This program calculates the future value of a child's RESP some time in the future assuming a constant deposit schedule\n")
    
    annual_deposit = eval(input("Hi, please enter the amount that will be deposited every year: "))
    growth_rate = eval(input("Enter the annualized interest rate that you think could be constantly earned by the account: "))
    n_years = eval(input("Enter the number of years the investment will be made for: "))
    
    investment_growth = 0
    for i in range(n_years):
              
        investment_growth += annual_deposit
        investment_growth *= (1 + growth_rate)  
        #print(investment_growth)
        
    print("The value of the RESP investment",n_years,"years from now will be:",'${:,.2f}'.format(investment_growth))
    
main()

'''
yearly = float(input("Enter the yearly investment: "))
apr = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years: "))

total = 0
for i in range(years):
    total += yearly
    total *= 1 + apr

print("The value in 12 years is: ", total)
'''