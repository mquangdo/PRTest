import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

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






# from matplotlib import pyplot as plt
# import numpy as np
# import random
#
# # Tạo ma trận 100x100x3 với giá trị ngẫu nhiên từ 0 đến 255
# image = np.random.randint(0, 2, (40, 40))
#
#
#
#
# plt.imshow(image)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Tạo đối tượng subplot
fig, ax = plt.subplots()

# Tạo một đối tượng plot rỗng
line, = ax.plot([], [], lw=2)


# Hàm khởi tạo
def init():
    # Thiết lập giới hạn trục x và y
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    return line,


# Hàm cập nhật dữ liệu
def update(frame):
    # Tạo dữ liệu mới cho plot
    xdata = np.linspace(0, 2 * np.pi, 100)
    ydata = np.sin(2 * np.pi * frame) * np.sin(xdata)

    # Cập nhật dữ liệu cho plot
    line.set_data(xdata, ydata)

    # Trả về đối tượng plot đã được cập nhật
    return line,


# Tạo đối tượng animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 200), init_func=init, blit=True)

# Hiển thị animation
plt.show()
