import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



N = 2 * 10

lwL = 2
lwR = 1
axRxlims = [0, N]
axRylims = [0, 160]

_t = np.linspace(0, N, N)
_y = (1 + np.sin(5 * _t))

dframe = np.full(N + 1, fill_value = np.nan, dtype = int)

t = np.tile(_t, (N, 1))
y = np.tile(_t, (N, 1))

for i in range(N):
    t[i, i + 1:] = np.nan
    y[i, i + 1:] = np.nan


fig, (axL, axR) = plt.subplots(ncols = 2, nrows = 1)
fig.suptitle('My plot')

for frame in range(N):
    axL.clear(), axR.clear()
    dframe[frame] = time.perf_counter()
    y2 = 1000 * np.diff(frame)
    y2_avg = np.nanmean(y2)
    axL.grid()
    axL.plot(t[frame], y[frame], lw = lwL)

    axR.grid()
    axL.plot(t[frame], y[frame], lw = lwR)
    fig.canvas.draw()

    plt.pause(0.00001)