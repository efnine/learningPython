#change.py
#   A program to calculate the value of some change in future dollars

def main():
    print("Change Counter")
    print("")
    print("Please enter the count of each coin type.")
    quarters = eval(input("How many quarters?: "))
    dimes = eval(input("How many dimes?: "))
    nickles = eval(input("How many nickles?: "))
    pennies = eval(input("How many pennies?: "))
    total = (quarters*0.25) + (dimes*0.10)+ (nickles*0.05)+ (pennies*0.01)
    print()
    print("The total value of your change is:","${:,.2f}".format(total))
    
main()
    
