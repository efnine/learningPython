def main():
    print("Lets figure out how much money Raphael could have for Harvard if we contribute every year some consistent amount")
    print()
    
    annual_deposit = eval(input("How much money will you contribute per annum? "))
    apr = eval(input("At what rate do you think the investment could grow? "))
    time_horizon = int(input("How long will the investment be held for? "))
    
    investment_value = 0
    for i in range(time_horizon):
        investment_value += annual_deposit
        investment_value *= (1+apr)
        
    print("After",time_horizon,"years, Raphael will likely have",'${:0,.2f}'.format(investment_value))
    
main()