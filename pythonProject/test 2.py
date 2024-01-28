import time

start = time.time()

pl = [2, 3]
for i in range(4, 1000000):
    stop = int(i ** 0.5)+1
    isP = True
    for p in pl:
        if p < stop:
            if i % p == 0:
                isP = False
                break
        else:
            break
    if isP:
        pl.append(i)

print(pl)
print()
print("Prime Count: "+str(len(pl)))
print("Time elapsed: {0} seconds.".format(time.time() - start))
