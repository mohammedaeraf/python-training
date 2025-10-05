import numpy as np
arr = np.array([1, 2, 3, 4, 5])

print(arr.sum())    # 15
print(arr.mean())   # 3.0
print(arr.min())    # 1
print(arr.max())    # 5

# Math functions
print(np.sqrt(arr)) # [1.   1.41 1.73 2.0  2.23]

# Reshape
mat = np.arange(1, 10).reshape(3, 3)
print(mat)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

