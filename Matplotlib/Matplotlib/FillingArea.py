import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('additonalFolder/data1.csv')#data là một dataframe
ages = data['Age']#lấy ra cột Age
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

print(data)

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287
another_median = 60000

plt.fill_between(ages, py_salaries, overall_median,where = py_salaries > overall_median, alpha = 0.25)
#fill_giữa trục ages(trục x) và đường py_salaries
#alha để làm mờ đi màu mình vừa fill để quan sát rõ hơn
#sau khi chạy ta sẽ thấy được fill ở giữa đường overall_median và
#py_salaries nhưng nếu ta thay ages = overall_median thì sẽ ko in ra gì

plt.fill_between(ages, py_salaries, overall_median,where = py_salaries <= overall_median, color = 'red', alpha = 0.25)


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
