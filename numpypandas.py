import numpy as np
my_first_array= np.array([1,2,3,4,5])
print("My first array;",my_first_array)
print("What type is it ;",type(my_first_array))
print("Numbet of dimensions:",my_first_array.ndim)
zeros_array=np.zeros(5)
print("\nAn array of zeros:",zeros_array)

ones_array=np.ones(3)
print("An array of ones:",ones_array)

grid_array=np.array([[10,20,30],[40,50,60]])
print("\nA 2D array (a grid):\n", grid_array)
print("It's shape (rows,columns):",grid_array.shape)
print

