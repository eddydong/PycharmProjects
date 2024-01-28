import numpy as np

np.set_printoptions(formatter={'float': lambda x: '%.4f' % x})


def sigmoid(x, deriv=False):
    if deriv:
        return x * (1 - x)
    else:
        return 1 / (1 + np.exp(-x))


def ReLU(x, deriv=False):
    if deriv:
        return np.where(x > 0, 1, 0)
    else:
        return np.where(x > 0, x, 0)


def lin(x, deriv=False):
    if deriv:
        return 0.1
    else:
        return 0.1*x

nonlin = ReLU


X = np.array([[3, 5, 3, 5],
              [4, 3, 3, 5],
              [5, 1, 3, 5],
              [6, 3, 3, 5]])

y = np.array([[16],
              [15],
              [14],
              [17]])

# np.random.seed(1)

l0Nodes = len(X[0])
l1Nodes = max(round(l0Nodes * 2 / 3), 3)
syn0 = 2 * np.random.random((l0Nodes, l1Nodes)) - 1
l2Nodes = len(y[0])
syn1 = 2 * np.random.random((l1Nodes, l2Nodes)) - 1

print("\n======= Neural Network with (with one hidden layers) =======")
print("==== Network Topology ", l0Nodes, " x ", l1Nodes, " x ", l2Nodes, " ====\n")

iterations = 1000
for j in range(iterations):

    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = l2 - y

    if (j % (int(iterations / 10)+1)) == 0:
        print("Err: " + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    # Updating weights (no alpha learning term here..)
    # Default Weight assignment equation : W = W + alpha.input.error
    syn1 -= 1 * l1.T.dot(l2_delta)
    syn0 -= 1 * l0.T.dot(l1_delta)

print("\nOutput after training ", iterations, " iterations")
print(l2)

# Testing a new data point
X = np.array([3, 6, 1, 1])
l0 = X
l1 = nonlin(np.dot(l0, syn0))
l2 = nonlin(np.dot(l1, syn1))

print("\n", l2)

# dic = ("<-", "|", "->")
#
#
# print("\nNew Data Test Result:")
# print(dic[np.argmax((l2))], max(l2))
