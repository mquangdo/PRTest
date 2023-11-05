import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from itertools import count

ax = plt.axes(projection = '3d')

# x = np.arange(-10,10,0.1)
# y = np.arange(-10, 10, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = X ** 2 + Y ** 2
# ax.plot_surface(X, Y, Z, cmap = 'plasma')
# plt.show()

index = count()
t = []

def draw(i):
    t.append(next(index) / 10)

    y1 = np.sin(np.array(t))
    y2 = np.cos(np.array(t))

    plt.cla()

    ax.plot3D(y1, y2, t)

ani = FuncAnimation(plt.gcf(), draw, interval = 10)

plt.show()