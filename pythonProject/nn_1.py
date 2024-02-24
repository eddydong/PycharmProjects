import numpy as np


# np.set_printoptions(formatter={'float': lambda x: '%.4f' % x})

def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


X = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1],

              [1, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 1, 0, 1, 0, 0, 1, 0],
              [0, 0, 0, 1, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 1, 0, 0, 1, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 1]
              ])

y = np.array([[0, 0, 1],
              [0, 0, 1],
              [0, 0, 1],
              [0, 0, 1],
              [0, 1, 0],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],

              [0, 0, 1],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],
              [1, 0, 0],
              [0, 0, 1],
              [1, 0, 0]
              ])

np.random.seed(1)

l0Nodes = len(X[0])
l1Nodes = max(round(l0Nodes * 2 / 3), 3)
syn0 = 2 * np.random.random((l0Nodes, l1Nodes)) - 1
l2Nodes = len(y[0])
syn1 = 2 * np.random.random((l1Nodes, l2Nodes)) - 1

print("\n======= Neural Network with (with one hidden layers) =======")
print("==== Network Topology ", l0Nodes, " x ", l1Nodes, " x ", l2Nodes, " ====\n")

iterations = 10000
for j in range(iterations):

    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = l2 - y
    if (j % round(iterations / 10)) == 0:
        print("Err: " + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    Learning_Rate = 0.1
    syn1 -= Learning_Rate * l1.T.dot(l2_delta)
    syn0 -= Learning_Rate * l0.T.dot(l1_delta)

# print("\nOutput after training ", iterations, " iterations")
# print(l2)

# Testing a new data point
X = np.array([0, 0, 0, 1, 1, 0, 1, 0, 0])
l0 = X
l1 = nonlin(np.dot(l0, syn0))
l2 = nonlin(np.dot(l1, syn1))

print()
print("Testing New Input", X)
print("Result:", l2)
dic = ("<-", "==", "->")
print("So the most likely move:", dic[np.argmax(l2)])
