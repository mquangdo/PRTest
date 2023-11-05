import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d





# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# x = y = np.arange(-10.0, 10.0, 0.1)
#
# g = lambda x: 2 * x
# f = lambda x: x
#
# plt.plot(x, g(x))
# plt.plot(x, f(x))
#
# X, Y = np.meshgrid(x, y)
# Z = X ** 2 + Y ** 2
#
# ax.plot_surface(X, Y, Z)
#
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
#
# plt.show()


ax = plt.axes(projection = '3d')
x_line = np.arange(-100, 100, 0.1)
y_line = np.arange(-100, 100, 0.1)
X , Y = np.meshgrid(x_line, y_line)
Z = X ** 2 + Y ** 2
ax.plot_surface(X, Y, Z, cmap = 'plasma', shade = True)

# t = np.arange(-10, 10, 0.1)  #polar coordinates
# x = np.cos(t)
# y = np.sin(t)
# ax.plot(x, y, t)

plt.show()