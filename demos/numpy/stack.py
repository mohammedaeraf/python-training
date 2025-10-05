import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.vstack([a,b]))
# [[1 2 3]
#  [4 5 6]]


arr = np.array([1,2,3])
view = arr.view()
copy = arr.copy()

arr[0] = 99
print(view)   # [99  2  3]
print(copy)   # [1 2 3]