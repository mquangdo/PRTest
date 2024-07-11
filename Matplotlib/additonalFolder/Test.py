import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 4000)
f = np.piecewise(x, [x >= 0, x <= 10], [lambda x: np.sin(x), lambda x: np.cos(x)])
plt.plot(x, f(x))

