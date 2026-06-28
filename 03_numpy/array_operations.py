# Array operations using NumPy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Element-wise add:", a + b)
print("Element-wise multiply:", a * b)
print("Square root:", np.sqrt(a))
print("Reshaped array:
", a.reshape(1, 3))
