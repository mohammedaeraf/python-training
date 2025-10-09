import numpy as np
a = np.array([[10,20,30],[40,50,60]])

print("Sum =", a.sum())
print("Row-wise Sum =", a.sum(axis=1))
print("Column-wise Sum =", a.sum(axis=0))
print("Mean =", a.mean())
print("Min =", a.min())
print("Max =", a.max())
