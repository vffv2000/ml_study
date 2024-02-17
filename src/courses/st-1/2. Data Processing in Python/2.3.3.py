# Задача № 3. На вход подаются данные, из которых создается датафрейм такой структуры:
#
#
#
# Ваша задача вывести датафрейм поменьше, но только с яблоками(apple), и чтобы цена на это яблоко, была больше 10.
#
# Важные моменты:
#
# Ответ выведите с использованием конструкции: print(df)
# Обратите внимание на индексы, нужно их переопределить, чтобы они начинались с нуля
# Строки должны распологаться в том же порядке что и у оригинального датафрейма
# Task No. 3. The input is data from which a dataframe of the following structure is created:
#
#
#
# Your task is to display a smaller dataframe, but only with apples, and so that the price of this apple is greater than 10.
#
# Important points:
#
# Print the answer using the construction: print(df)
# Pay attention to the indexes, you need to redefine them so that they start from zero
# Rows must be in the same order as the original dataframe
# Sample Input:
#
# apple banana orange
# 0.14 0.35 0.84 0.64 0.68 0.22 0.94 0.48 0.29
# 12 6 11 2 3 12 7 19 7
# Sample Output:
#
#    fruit  rating  price
# 0  apple    0.14     12