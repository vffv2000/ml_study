# Задача № 4.  На вход подаются данные, из которых создается датафрейм, состоящий из n * n элементов. При n = 6,
# выглядит он так:
#
#
# Ваша задача найти суммы элементов главной и побочной диагонали. Нужно вывести 2 числа через пробел.
#
# Главная диагональ - от верхнего левого угла, до нижнего правого
#
# Побочная диагональ - он нижнего левого угла, до верхнего правого
#
# Task No. 4. Data is supplied as input, from which a dataframe consisting of n * n elements is created.
# With n = 6, it looks like this:
#
# Your task is to find the sum of the elements of the main and secondary diagonals.
# You need to print 2 numbers separated by a space.
#
# Main diagonal - from the upper left corner to the lower right
#
# Side diagonal - it is from the bottom left corner, to the top right
#
# Sample Input:
#
# 13 17 1 2 7 1 18 7 11 18 4 7 15 3 5 17 3 13 3 3 2 18 19 11 10
# Sample Output:
#
# 59 38

import pandas as pd
import numpy as np

data = '13 17 1 2 7 1 18 7 11 18 4 7 15 3 5 17 3 13 3 3 2 18 19 11 10'
data = np.array([int(i) for i in data.split(" ")])
n = int(len(data) ** 0.5)
data = np.reshape(data, (n, n))
df = pd.DataFrame(data = data)

# Your code here
main_diagonal_sum = np.trace(df)

secondary_diagonal_sum = np.trace(np.fliplr(df))

print(main_diagonal_sum, secondary_diagonal_sum)
