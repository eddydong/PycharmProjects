# Polynominal Linear Regression from scratch
# by Eddy K. Dong, Jan 28, 2024
#
# This is to estimate a polynomial function using Gradient Descend algorithm. The function is defined as y = a1 * x1
# + a2 * x2 + ... an * xn + bias Given O observations (X's, or [x1, x2, ... xn]'s, and Y's), it tries to find the
# best set of a1..an to minimize the MSE x1, x2... can be non-linear products of another observation, so that it can
# do non-linear estimations

import numpy as np

np.random.seed(0)


class Train:
    def __init__(self, xo, yo):
        self.O = len(xo)
        self.N = len(xo[0])
        self.xo = np.insert(xo, self.N, np.ones(self.O), axis=1)
        self.yo = yo
        self.A = None
        self.estimate()

    def E(self, A):
        e = np.dot(self.xo, A)
        return np.mean((e - self.yo) ** 2)

    def estimate(self, it=10000, lr=0.001, st=1e-8):
        A = np.random.rand(self.N + 1, 1)
        Al = np.random.rand(self.N + 1, 1)
        error = None
        iterated = None
        dl = None
        for i in range(it):
            iterated = i
            d = []
            for k in range(self.N + 1):
                Ap = Al.copy()
                Ap[k] = A[k]
                try:
                    dd = (self.E(Ap) - self.E(Al)) / (A[k] - Al[k])
                except:
                    dd = dl[k]
                d.append(dd)
            dl = d.copy()

            # if (float('nan') in d or float('inf') in d
            #         or float('-inf') in d or 0.0 in d):
            #     print(i, d)

            Al = A.copy()
            A -= lr * np.array(d)
            error = self.E(A)
            if abs(error) < st:
                break
        self.A = A
        return error, iterated

    def predict(self, xo):
        xo = np.insert(xo, len(xo[0]), np.ones(len(xo)), axis=1)
        return np.dot(xo, self.A)
