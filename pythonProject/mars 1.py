def N(n):
    if n == 1:
        return [2, 1]
    elif n == 2:
        return [3, 2]
    else:
        n1, n2 = N(n-1), N(n-2)
        return [n1[0] + n2[0],
                n1[1] + n2[1]]

print(N(20))
