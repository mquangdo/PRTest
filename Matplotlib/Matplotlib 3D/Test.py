import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from itertools import count

parameter = count()
index = []


domain: np.ndarray = np.arange(-50, 50, 0.1)
ax = plt.axes(projection = '3d')

def update(i) -> None:
    ax.set_xlim(0, 105)
    ax.set_ylim(0, 12)
    y1: np.ndarray = domain
    y2: np.ndarray = domain
    X, Y = np.meshgrid(y1, y2)
    Z = np.cos(next(parameter) / 1000 * X) * np.sin(next(parameter) / 1000 * Y)
    ax.cla()
    ax.plot_surface(X, Y, Z, cmap = 'plasma')


animate = FuncAnimation(plt.gcf(), update, interval = 0.1)
plt.show()





