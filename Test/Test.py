import numpy as np
import time
import pandas as pd

loveDf = pd.DataFrame({
           'I': ['love','you','so','much'],
          'But': ['you','dont','love','me'],
          'So': ['I','am','broken','huhu']})
print(loveDf)

print(loveDf.iloc[2])
print()

boysDf = pd.read_csv('data.csv')
print(boysDf)


# temperatures = np.array([
#        29.3, 42.1, 18.8, 16.1, 38.0, 12.5,
#         12.6, 49.9, 38.6, 31.3, 9.2, 22.2
#     ]).reshape(2, 2, 3)
#
# print(temperatures)
# print()
#
# print(np.swapaxes(temperatures, 0, 1))

# square = np.array([
#         [16, 3, 2, 13],
#         [5, 10, 11, 8],
#         [9, 6, 7, 12],
#         [4, 15, 14, 1]
#     ])
#
# print(square % 4 ==0)
# mask = square % 4 == 0
# print(mask)
#
# print(square[mask])
# import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)

output = img.copy()  # The original image is read-only!
output[:, :, :1] = 0
mpimg.imsave("blue.jpg", output)

df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

print(df)
print(pd.melt(df, id_vars=['A'], value_vars=['B']))


import pandas as pd
import requests

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")

pd.set_option("display.max.columns", None)
# pd.set_option("display.precision", 2)
nba = pd.read_csv("nba_all_elo.csv")
# print(nba)
# print(nba.head())
# print(nba.info)
print(nba.describe(include = object))

import matplotlib
nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()

import numpy as np
from matplotlib import pyplot as plt

# initialize function
f = lambda x: np.sin(2 * np.pi * x)
g = lambda x: np.cos(2 * np.pi * x)

# split lower bound and upper bound into 1000 range by 1001 points
lb, ub = -2, 2
x = np.linspace(lb, ub, 1001)
y1 = f(x)
y2 = g(x)

# plot
# plt.figure(figsize=(15, 10))
# plt.plot(x, y1, '--', color='blue', label='sin(x)')
# plt.plot(x, y2, '-', color='red', label='cos(x)')
# plt.xlabel('x', fontsize=14)
# plt.ylabel('y', fontsize=14)
# plt.title('Draw sin(x) and cos(x)', fontsize=18)
# plt.legend(fontsize=14)
# plt.grid()
# plt.savefig('demo-matplotlib.png')
# plt.show()

# plt.style.use('fivethirtyeight')
# plt.title('Test')
# plt.xlabel('Ages')
# plt.ylabel('Salaries')
#
# dev_x = [25,26,27,28,29,30,31,32,33]
# dev_y = [10,20,45,67,89,90,100,211,321]
# plt.plot(dev_x, dev_y,color = 'k', linestyle ='--',marker = 'o',linewidth ='2' ,label = 'First test')
#
# py_dev_y  = [1,2,3,4,5,6,7,8,1000]
# plt.plot(dev_x, py_dev_y,'b',marker = 'o' ,label = 'Second test')
#
# plt.legend()
# plt.tight_layout()
# # plt.grid(True)
#
#
#
# plt.show()



from mpl_toolkits.mplot3d import axes3d
# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection = '3d')
#
# x = np.linspace(-5,5,100)
# y = np.linspace(-5,5,100)
# z = lambda x, y : x * y
# z1 = z(x,y)
#
# ax1.plot_wireframe(x,y,z1)
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-10.0, 10.0, 0.1)
X, Y = np.meshgrid(x, y)
Z = X ** 2 + Y ** 2

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()








