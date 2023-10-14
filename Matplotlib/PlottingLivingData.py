import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')



ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()









# from itertools import count
# index = count() #tạo ra một đối tượng count vô hạn như bài trước
#
# x_vals = []
# for i in range(8):
#     x_vals.append(next(index)) #truy cập vào phần tử tiếp theo bằng next()
# print(x_vals) #[0, 1, 2, 3, 4, 5, 6, 7, 8]