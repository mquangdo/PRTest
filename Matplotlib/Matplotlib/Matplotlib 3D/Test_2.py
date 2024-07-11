import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation
import math

index = count()
x_data = []

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)

ax1.set_xlim(0, 20)
ax1.set_ylim(-2,2)
ax1.grid('True')

ax2.set_xlim(0, 20)
ax2.set_ylim(-2,2)
ax2.grid('True')

ax3.set_xlim(0, 20)
ax3.set_ylim(-2,2)
ax3.grid('True')

ax4.set_xlim(0, 20)
ax4.set_ylim(-2,2)
ax4.grid('True')

line_1, = ax1.plot(0, 0)
line_2, = ax2.plot(0, 0)

def animate(i):
        x_data.append(next(index) / 10)

        y1 = np.sin(x_data)
        y2 = 1 * np.cos(x_data)

        line_1.set_xdata(x_data)
        line_1.set_ydata(y1)

        line_2.set_xdata(x_data)
        line_2.set_ydata(y2)



ani = FuncAnimation(plt.gcf(), animate, frames = np.arange(0, 10, 0.001), interval=10)
plt.show()