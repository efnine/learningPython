import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_by_cities.csv')
print(df)
print('------------------------------------------------------')


grouped_df = df.groupby('city')
print(grouped_df.get_group('mumbai'))
print('------------------------------------------------------')

print("Lets print")
for city, city_df in grouped_df:
    print(city)
    print(city_df)
        

print('------------------------------------------------------')
print(grouped_df.max())


print('------------------------------------------------------')
print(grouped_df.mean())

print('------------------------------------------------------')
print(grouped_df.describe())

print('------------------------------------------------------')
print("Here we go!")
print(grouped_df['city'])
print('------------------------------------------------------')

print("Lets plot!")
### lets plot this bitch
colors = ['r','g'] # there many more colors 
# Code    Color
# b    blue
# g    green
# r    red
# c    cyan
# m    magenta
# y    yellow
# k    black
# w    white
color_index = 0
for city, city_df in grouped_df:
    color = colors[color_index]
    group_label = city[0]
    group_data = city[1]
    plt.plot(grouped_df.get_group('mumbai'),color=color,label=group_label)
    color_index += 1
    plt.show()

    
# plt.plot(grouped_df.describe(),label='My Data')
# plt.xlabel('Index')
# plt.ylabel('Plot Value')
# plt.title('The Plot Value From surveys.csv')
# # grouped_df.groupby('class').hist()
# plt.show()