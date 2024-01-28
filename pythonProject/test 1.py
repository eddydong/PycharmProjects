def fb(n):
    if n > 2:
        return fb(n-1)+fb(n-2)
    else:
        return 1


for i in range(20):
    print(fb(i+1))
