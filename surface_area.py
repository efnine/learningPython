# surface_area.py
#   A program to calculate the surface and area of a sphere from the radious given user input
import math

def main():
    print("\nLets calculate the volume and area of a sphere!")
    rad = eval(input("What is the radious? "))
    
    pi = math.pi
    volume = round((4 / 3) * pi * rad**3)
    area = round(4 * pi * rad**2)
    
    print("The volume is approximately:",volume,"m^3")
    print("The area is approximately:",area)
    main()
    
main()