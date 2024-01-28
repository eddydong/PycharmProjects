import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=plt.figaspect(0.6))
grid = plt.GridSpec(2, 3, wspace=0.5, hspace=0.5)

#np.random.seed(0)
xo = np.random.rand(10) * 10
eo = np.random.rand(10)
yo = 0.5 * xo - 7 + eo


def E(a, b):
    s = sum((yo - (a * xo + b)) ** 2)
    return s / len(xo) / 2


route = []
desc = []


def optim(it):
    alpha = 0.01
    a, b = 18, 15
    al, bl, el = 0, 0, 0
    for i in range(it):
        d_a = ((E(a, bl) - E(al, bl))
               / (a - al))
        d_b = ((E(al, b) - E(al, bl))
               / (b - bl))
        al = a
        bl = b
        a -= alpha * d_a
        b -= alpha * d_b
        e = E(a, b)
        de = e - el
        desc.append([i, e])
        el = e
        print(i, e)
        route.append([a, b, e])
        if abs(de) < 1e-6:
            break
    return [a, b]


r = optim(10000)

res = []
for i in range(20):
    for j in range(20):
        aa = i * 2 - 20
        bb = j * 2 - 20
        res.append([aa, bb, E(aa, bb)])

res = np.transpose(res)
route = np.transpose(route)
desc = np.transpose(desc)

# Draw Observations

ax = plt.subplot(grid[0, 0])
ax.set_title('Observations')
ax.scatter(xo, yo, c="green")
x1, x2 = min(xo), max(xo)
ax.plot([x1, x2], [r[0] * x1 + r[1],
                  r[0] * x2 + r[1]], "red")

# Draw Err descend

ax = plt.subplot(grid[1, 0])
ax.set_title('Error Descend')
ax.plot(desc[0], desc[1])

# Draw Error Plane
ax = plt.subplot(grid[0:2, 1:3], projection="3d")
ax.scatter3D(res[0], res[1], res[2], c="lightblue")
ax.plot3D(route[0], route[1], route[2], c="red")
ax.scatter3D([0.5], [-7], [E(0.5, -7)], c="green")
ax.set_title('Error Plane')
ax.set_xlabel("a")
ax.set_ylabel("b")
ax.set_zlabel("Err")

plt.show()
