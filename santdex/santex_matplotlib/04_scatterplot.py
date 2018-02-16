import matplotlib.pyplot as plt

### scatter
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,3,4,5,8,9]

plt.scatter(x,y, label='skitscat', color='k', s=10)

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')
plt.title('Interesting Title\nCheck Out Subtitle')
plt.legend()


plt.show()