from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
colors = ['blue', 'red', 'yellow', 'pink', 'purple']
explode = [0, 0, 0.1, 0, 0]

plt.pie(slices, labels = labels, colors = colors , shadow = True, explode = explode, autopct = '%1.1f%%', wedgeprops = {'edgecolor':'black'})
#wedgeprops = {'edgecolor':'black'} thêm viền đen
#them color duoi dang mot list
#explode nhu la kieu tach roi 1 miếng pie ra
#shadow thêm bóng
#autopercentage


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f