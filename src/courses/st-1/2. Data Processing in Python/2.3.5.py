# Задача № 5 . На вход подаются данные, из которых создается датафрейм такой структуры:
#
#
#
# Посчитайте среднее значение цен на каждый вид фруктов. В результате должна быть таблица, имеющая 2 столбца,
# вид фрукта и средняя цена на этот вид.
#
# Indicate the average price for each type of fruit. The result should be a table with 2 columns,
# the type of fruit and the average price for this type.
#
# Важные моменты:
#
# Столбец со средней ценой окуруглите до 2-х знаков после точки.
# Ответ выведите с использованием конструкции: print(df)
# Обратите внимание на индексы, их нужно оставить, возможно для этого нужно использовать какой нибудь параметр метода groupby(https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
# Sample Input:
#
# apple banana orange
# 0.14 0.35 0.84 0.64 0.68 0.22 0.94 0.48 0.29
# 12 6 11 2 3 12 7 4 7
# Sample Output:
#
#     fruit  price
# 0   apple   7.00
# 1  banana   4.33
# 2  orange  10.00


import pandas as pd

# Преобразование входных данных
fruits = ["apple", "banana", "orange"] * 3
ratings = [0.14, 0.35, 0.84, 0.64, 0.68, 0.22, 0.94, 0.48, 0.29]
prices = [12, 6, 11, 12, 3, 12, 7, 19, 7]
# Создание DataFrame
df = pd.DataFrame({'fruit': fruits,
                   'rating': ratings,
                   'price': prices})

# apple banana orange
# 0.14 0.35 0.84 0.64 0.68 0.22 0.94 0.48 0.29
# 12 6 11 2 3 12 7 4 7
# Создание датафрейма


# Your code here

average_price_per_fruit = df.groupby('fruit')['price'].mean().reset_index()
average_price_per_fruit['price'] = average_price_per_fruit['price'].map('{:.2f}'.format)

print(average_price_per_fruit)