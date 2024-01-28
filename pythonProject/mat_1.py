import numpy as np

a = np.mat(np.array(
    [[1, 0, 2],
     [-1, 3, 1],
     [3, 1, 3]]))

b = np.mat(np.array(
    [[3],
     [3],
     [4]]))

print(a.I * b)
