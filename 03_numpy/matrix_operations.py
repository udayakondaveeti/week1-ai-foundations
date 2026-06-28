# Matrix operations with NumPy
import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:
", matrix_a)
print("Matrix B:
", matrix_b)
print("Matrix product:
", np.dot(matrix_a, matrix_b))
print("Transpose of A:
", matrix_a.T)
