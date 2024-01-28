# Polynominal Regression from scratch
# by Eddy K. Dong, Jan 28, 2024
#
# This is to estimate a polynomial function using Gradient Descend algorithm.
# The functions is defined as y = a1 * x1 + a2 * x2 + ... an * xn + bias
# Given M observations (X's, or [x1, x2, ... xn]'s, and Y's), it tries to find the best set of a1..an to minimize the MSE
# x1, x2... can be non-linear products of another observation, so that it can do non-linear estimations

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

# Global Constants
N = 4  # number of independent variables, not including the bias
M = 100  # number of observations

# Define Observations
xo = np.random.rand(M, N+1) * 10
xo[:, N] = 1
Ao = np.random.rand(N+1, 1)
yo = np.dot(xo, Ao)
#print(xo, "\n\n", Ao, "\n\n", yo)

plot_data = []

# Define the error function
def E(A):
    e = np.dot(xo, A)
    return np.mean((e-yo)**2)


def estimate(it):
    alpha = 0.001
    A = np.random.rand(N + 1, 1)
    Al = np.zeros((N + 1, 1))-1
    el = float('inf')
    for i in range(it):
        d = []
        for k in range(N + 1):
            Ap = []
            for j in range(N + 1):
                if k == j:
                    Ap.append(A[j])
                else:
                    Ap.append(Al[j])
            d.append((E(Ap) - E(Al))
                     / (A[k] - Al[k]))
        Al = A.copy()
        A -= alpha * np.array(d)
        e = E(A)
        de = e - el
        el = e
        if i % 1000 == 0:
            print(i, e)
        plot_data.append(e)
        if abs(de) < alpha * 1e-7:
            break
    return A

print("estimated:\n", estimate(100000))
print("actual:\n", Ao)

plt.plot(plot_data)
plt.show()

