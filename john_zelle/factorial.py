# factorial.py
#   This program askss the user for an integer and then proceeds to tell the user the number of 
# of permuations available

def main():
    n = eval(input("Please enter a whole number: "))
    factorial = 1
    for factor in range(n,1,-1):
        factorial = factorial * factor
        print(factorial)
    print("\nThe factorial of",n,"is",factorial)
    print()
    main()
    
main()

