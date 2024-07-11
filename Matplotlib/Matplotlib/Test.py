import matplotlib.pyplot as plt
import numpy as np

plt.xlim([0, 4])
plt.ylim([0, 4])
x = np.linspace(0, 4, 1000)
y = lambda x: 4 - x/2
g = lambda x: 2
plt.plot(x, y(x), color='black')
# plt.plot(x, g(x), color ='black')
plt.fill_between(g(x), y(x), color = 'red')
print(y(x))


