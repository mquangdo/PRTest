import pandas as pd

# revenues = pd.Series([5555,7000,1980])
# print(revenues)
# print(revenues.values)
#
# df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
#                    'B': {0: 1, 1: 3, 2: 5},
#                    'C': {0: 2, 1: 4, 2: 6}})
#
# print(df.values)
# print(df.index)
# print(revenues.index)
# colors = pd.Series(
#      ["red", "purple", "blue", "green", "yellow"],
#     index=['damn', 2, 3, 'damn2', 8])
#
# print(colors.loc['damn':'damn2'])
#
# toys = pd.DataFrame([
#      {"name": "ball", "shape": "sphere"},
#     {"name": "Rubik's cube", "shape": "cube"}])
#
# print(toys)

further_city_data = pd.DataFrame(
    {"revenue": [7000, 3400], "employee_count":[2, 2]},
    index=["New York", "Barcelona"])

print(further_city_data)
print()

city_revenues = pd.Series([4200,6000,6500],index = ['Amsterdam','Toronto','Tokyo'])
city_employee_count = pd.Series({'Amsterdam':5, 'Tokyo':8
})
city_data = pd.DataFrame({'revenue':city_revenues, 'employee_count':city_employee_count})

print(city_data)
print()

all_city_data = pd.concat([city_data, further_city_data],axis = 0, sort=False)
print(all_city_data)
print()



city_countries = pd.DataFrame({
     "country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
    "capital": [1, 1, 0, 0, 0]},
    index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"])
print(city_countries)
print()

cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
print(cities)


