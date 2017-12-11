from math import sqrt

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j = num / i
            print("%d equals %d * %d" % (num, i ,j))
            break
    else:
        print(num, "is a prime number")

"""
fruits = ["apple","orange","banana"]

for i in range(len(fruits)):
    print("Current fruit: ",fruits[i])
    


color = ["red"]

for i in color[:]:
	if i == "red":
		color += ["black"]
	if i == "black":
		color += ["white"]
print(color)


n = int(input("Maximal number? "))

for a in range (1,n+1):
    for b in range (a,n):
        c_sqr = a ** 2 + b**2
        c = int(sqrt(c_sqr))
        if ((c_sqr - c**2) == 0):
            print (a,b,c)

"""


