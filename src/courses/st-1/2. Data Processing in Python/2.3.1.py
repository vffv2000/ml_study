# Задача № 1. На вход подается строка из букв, которая далее преобразовывается в серию Ваша задача посчитать сколько
# раз встречается каждая буква. Вывод нужно организовать в формате: print(pd.Series). Также отсортируйте серию
# в порядке возрастания.
#
#
# Task No. 1. The input is a string of letters, which is then converted into a series. Your task is to count how many
# times each letter appears. The output should be organized in the format: print(pd.Series). Also sort the series
# in ascending order.
# Sample Input:
#
# endqbednnceeeqbqndqenbmndbqdqeeqdqbmwwqneccwccmmmcbqcbndbmqdbdbbqdcecdwqqb
# Sample Output:
#
# w     4
# m     6
# n     8
# c     9
# e    10
# d    11
# b    12
# q    14
# dtype: int64

import pandas as pd

user_input = input("")
ser = pd.Series(list(user_input))
print(ser.value_counts(ascending=True))