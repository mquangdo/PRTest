import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]


#s: độ to nhỏ cuủa các chấm
#c : màu, hay nói đúng hơn là 1 list các cấp độ màu
#marker: hình dạng các chấm, ví dụ thay dấu chấm thành dấu x
#cmap: là màu, còn color ở trên chỉ là các cấp độ màu của cmap Blues





sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c = ratio, cmap = 'summer', edgecolors = 'black')
#ta có thể lấy ngay các phần tử trong list để làm list màu như c = ratio
# nghĩa là màu càng sáng màu thì giá trị càng lớn

plt.xscale('log')
plt.yscale('log')
#2 dòng này giúp ta nhìn rõ các điểm mà không bị díu dít


cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()