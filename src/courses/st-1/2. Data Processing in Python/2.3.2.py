# Задача № 2. На вход подаются данные, из которых создается датафрейм, состоящий из 25 элементов(5 строк, 5 столбцов).
# Выглядит он так:
#
# Task No. 2. The input is data from which a dataframe is created, consisting of 25 elements (5 rows, 5 columns).
# Looks like that:
#
# Ваша задача найту сумму элементов с адресами: (3;a), (1; c), (0; e)
#
# Важные моменты:
#
# Sample Input:
#
# 7 15 7 18 2 6 9 10 2 8 11 19 9 5 8 10 4 14 6 19 17 1 12 1 13
# Sample Output:
#
# 22


import pandas as pd
import numpy as np

# Обработка входных данных
data = input()
data = np.array([int(i) for i in data.split(" ")])
data = np.reshape(data, (5, 5))
df = pd.DataFrame(data = data, columns=list('abcde'))

coord = [(3, 'a'), (1, 'c'), (0, 'e')]
answer = sum([df.loc[c] for c in coord])
print(answer)