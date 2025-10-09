import numpy as np

arr = np.array([10, 25, 30, 45, 50])

print(arr > 30)      # [False False False  True  True]
print(arr[arr > 30]) # [45 50]