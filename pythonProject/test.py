def safeDiv(num, den):
    sysMin = 1e-323
    sysMax = 1e308
    if num == 0.0:
        num = sysMin
    if den == 0.0:
        den = sysMin

    def getE(n):
        n_s = str("%e" % n)
        n_e_pos = n_s.find('e') + 1
        return int(n_s[n_e_pos:])

    num_e = getE(num)
    den_e = getE(den)
    while num_e < -100 or den_e < -100:
        num = num * 10
        den = den * 10
        num_e = getE(num)
        den_e = getE(den)
    return num / den


# print(1e-100 / 1e-400)
# print(safeDiv(100, 1e-900))
#print(1e308)

def test(a, b):
    return a/b

try:
    print(test(10, 0))
except:
    print("err")