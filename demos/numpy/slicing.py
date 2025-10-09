import numpy as np
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])

print(arr[0, 1])     # Element at 1st row, 2nd col
print(arr[1, :])     # Entire 2nd row
print(arr[:, 2])     # Entire 3rd column
print(arr[0:2, 0:2]) # Submatrix
