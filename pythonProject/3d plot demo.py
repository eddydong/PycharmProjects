from matplotlib import pyplot as plt
import numpy as np

x, y = np.mgrid[-1:1:50j, -1:1:50j]
z = x**2 + y**3
ax = plt.figure(figsize=(10, 8)).add_subplot(111, projection='3d')
ax.plot_wireframe(x, y, z, **{'rstride':1, 'cstride':1})
ax.plot([0], [0], [0], 'rx')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
