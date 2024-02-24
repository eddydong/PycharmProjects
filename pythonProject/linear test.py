import linear
import time

xo = [[2],
      [3],
      [4],
      [50]]

yo = [[5],
      [7],
      [9],
      [11]]

t = time.time()
m = linear.Train(xo, yo)
#print(m.predict([[10]]))
#print("time: " + str(time.time()-t))
