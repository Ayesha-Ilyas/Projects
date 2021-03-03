# importing Numpy package
import numpy as np

# creating a 2X2 Numpy matrix
n_array = np.array([[60, 28], [65, 54]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 2X2 matrix:")
print(int(det))