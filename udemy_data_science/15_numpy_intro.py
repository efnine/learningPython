import numpy as np

 # numpy arrays come in 2 flavours:
 # vectors --> 1d shapes
 # matrices --> 2-d shapes 
 
my_lst = [1,2,3]
arr = np.array(my_lst)
print(arr)
print('-------------------------------\n')

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(my_mat)
print(arr2)
print('-------------------------------\n')
 
### common ways to create a numpy array ###
numpy_range = np.arange(0,10,3) # works like python 'range' function
print(numpy_range)
print('-------------------------------\n')

numpy_zeros = np.zeros((5,7))
print(numpy_zeros)
print('-------------------------------\n')

numpy_linspace = np.linspace(0,5,25) # different than range
print(numpy_linspace)
print('-------------------------------\n')

### identity matrix ###
numpy_id_matrix = np.eye(4)
print(numpy_id_matrix)
print('-------------------------------\n')

### random numbers ###
numpy_random = np.random.rand(5,5)
print(numpy_random)
print('-------------------------------\n')

numpy_random_gaussian = np.random.randn(5,5)
print(numpy_random_gaussian)
print('-------------------------------\n')

numpy_random_random = np.random.randint(0,100,50)
print(numpy_random_random)
print('-------------------------------\n')

arr = np.arange(25)
numpy_reshape = arr.reshape(5,5)
print(numpy_reshape)
print('-------------------------------\n')


numpy_random_random = np.random.randint(0,100,50)
print("Min is:")
print(numpy_random_random.argmin())
print("Max is:")
print(numpy_random_random.argmax())
print('-------------------------------\n')

numpy_random_random = np.random.randint(0,100,50)
print(numpy_random_random.shape)
print(numpy_random_random.dtype)
print('-------------------------------\n')









































