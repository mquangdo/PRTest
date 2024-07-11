import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time
from itertools import count

# x = np.arange(-10,10,0.1)
# y = np.arange(-10, 10, 0.1)
# X, Y = np.meshgrid(x, y)
# Z = X ** 2 + Y ** 2
# ax.plot_surface(X, Y, Z, cmap = 'plasma')
# plt.show()

index = count()
t = []
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 100)
f = lambda x: (18 - 3 * x) / 2
g = lambda x: (2 + x) / 2


def draw(i):
    t.append(next(index) / 10)
    y1 = f(np.array(t))
    y2 = g(np.array(t))
    plt.cla()
    ax.plot(y1, t)
    ax.plot(y2, t)
ani = FuncAnimation(plt.gcf(), draw, interval = 10)
plt.show()