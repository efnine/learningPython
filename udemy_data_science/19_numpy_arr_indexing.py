import numpy as np


### indexing a 1d array ###
arr = np.arange(0,11)

print(arr[1:5]) # one can slice and indexing just like a py list
print(arr[:6]) # one can slice and indexing just like a py list
print(arr[1:]) # one can slice and indexing just like a py list
print('-------------------------------\n')

py_lst = [1,2,3,4,5,6]
print(py_lst[:4])
print('-------------------------------\n')

arr = np.arange(0,11)
arr[0:5] = 100
print(arr)
print('-------------------------------\n')
arr = np.arange(0,11)
arr[:] = 8
print(arr)
print('-------------------------------\n')
arr = np.arange(0,11)
arr_copy = arr.copy()
arr[:] = 8
print("Notice how the numpy array changes:")
print(arr)
print('-------------------------------\n')
print("Notice how the numpy copy array DOES NOT change:")
print(arr_copy)
print('-------------------------------\n')


### indexing a 2d array ###
arr_2df = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2df)
print('-------------------------------\n')

# grabing elements from a 2d array
print('-------------------------------\n')
print("Double bracket method:")
print(arr_2df[0][2])
print('-------------------------------\n')

print('-------------------------------\n')
print("Single bracket method (recommended):")
print(arr_2df[0,2])
print('-------------------------------\n')

# grabing chunks from a 2d array
print('-------------------------------\n')
print("Retrieving a matrix chuck:")
print(arr_2df[1:,:2])
print('-------------------------------\n')


### conditional selection ###
arr = np.arange(1,11)
bool_arr = arr > 5

print('-------------------------------\n')
print("Conditional selection boll_arr:")
print(arr)
print(arr[arr > 5])
print(arr[arr < 5])
print(arr[bool_arr])
print('-------------------------------\n')

print('-------------------------------\n')
print("End of lecture exercise:")
arr = np.arange(50).reshape(5,10)
print(arr)
print(arr[arr > 25])
print(arr[arr < 25])
print(arr[3:,2:5])
print('-------------------------------\n')


































