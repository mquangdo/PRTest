from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
from matplotlib.animation import FuncAnimation

with open('additonalFolder/data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) #đọc từ điển ra 1 doi tuong iterable

    language_counter = Counter() #tạo ra một đối tượng đếm, ở đây language_counter là một từ điển
                                 #với key là các ngôn ngữ, và value là số lần xuất hiện

    #VD
    # counter = Counter()
    # counter.update(['python', 'java'])
    # counter.update(['python', 'java'])
    # print(counter)  ->>>   Counter({'python': 2, 'java': 2})


    row = next(csv_reader)#iterable có thể truy cập bằng phương thức next()
    print(row)#{'Responder_id': '1', 'LanguagesWorkedWith': 'HTML/CSS;Java;JavaScript;Python'}
    #row['LanguagesWorkedWith'] đây là 1 list, đúng hơn là 1 value của key languagesworkedwith

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))#tham số là một list, .update sẽ đếm số phần tử giống nhau trong list


# print(language_counter)
# print(language_counter.most_common(15))


language = []
popularity = []

for i, v in language_counter.most_common(15):
    language.append(i)
    popularity.append(v)

# print(language)
# print(popularity)

plt.barh(language, popularity) #barh để đổi axes
plt.title('Most popular programming languages')
plt.xlabel('Programming language')
plt.ylabel('Number of people used')

plt.tight_layout()
plt.show()

# plt.style.use("fivethirtyeight")
#
# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
#
# x_index = np.arange(len(ages_x))
# width = 0.25
#
# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]
# plt.bar(x_index - width, dev_y,width = width, color="#444444", label="All Devs")
#
# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]
# plt.bar(x_index, py_dev_y, width = width,color="#008fd5", label="Python")
#
# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]
# plt.bar(x_index + width, js_dev_y, width = width, color="#e5ae38", label="JavaScript")
#
# plt.legend()
#
# plt.xticks(ticks = x_index, labels = ages_x)
#
#
# plt.title("Median Salary (USD) by Age")
# plt.xlabel("Ages")
# plt.ylabel("Median Salary (USD)")
#
# plt.tight_layout()
#
# plt.show()

from itertools import count

index = count()
x = []