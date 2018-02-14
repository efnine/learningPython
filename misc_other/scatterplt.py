import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,]

y = [23,34,76,80,25,78,65,90,100]

plt.scatter(x,y,label='skitscat',color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()