import numpy as np

map = np.zeros((8, 8), dtype=int)
res = []


def legal(m, y, x):
    if sum(m[:, x]) > 0 or sum(m[y, :]) > 0:
        return False
    for yy in range(8):
        for xx in range(8):
            if (yy - y == xx - x or yy - y == x - xx) and m[yy, xx] == 1:
                return False
    return True


def search(y, m):
    if y == 8:
        res.append(m)
        return
    else:
        for x in range(8):
            if legal(m, y, x):
                m[y, x] = 1
                search(y + 1, m.copy())
                m[y, x] = 0


search(0, map)
for i in range(len(res)):
    print(np.array(res[i]))
print("Total: " + str(len(res)))
