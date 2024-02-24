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


for y0 in range(8):
    if legal(map, 0, y0):
        map[0][y0] = 1
        for y1 in range(8):
            if legal(map, 1, y1):
                map[1][y1] = 1
                for y2 in range(8):
                    if legal(map, 2, y2):
                        map[2][y2] = 1
                        for y3 in range(8):
                            if legal(map, 3, y3):
                                map[3][y3] = 1
                                for y4 in range(8):
                                    if legal(map, 4, y4):
                                        map[4][y4] = 1
                                        for y5 in range(8):
                                            if legal(map, 5, y5):
                                                map[5][y5] = 1
                                                for y6 in range(8):
                                                    if legal(map, 6, y6):
                                                        map[6][y6] = 1
                                                        for y7 in range(8):
                                                            if legal(map, 7, y7):
                                                                map[7][y7] = 1
                                                                res.append(map.copy())
                                                            map[7][y7] = 0
                                                    map[6][y6] = 0
                                            map[5][y5] = 0
                                    map[4][y4] = 0
                            map[3][y3] = 0
                    map[2][y2] = 0
                map[1][y1] = 0
        map[0][y0] = 0

print(res)
print(len(res))