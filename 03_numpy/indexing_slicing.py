# Indexing and slicing with NumPy
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Slice:", arr[1:4])
print("Even values:", arr[arr % 2 == 0])
