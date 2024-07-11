import matplotlib.pyplot as plt
import numpy as np
import random
from itertools import count

parameter = count()
index = []

for i in range(1000):
    index.append(next(parameter) / 100)
    plt.plot(index, np.sin(index))
    plt.pause(0.01)
    plt.cla()

plt.xlim([0, 20])
plt.ylim([0,10])
plt.show()