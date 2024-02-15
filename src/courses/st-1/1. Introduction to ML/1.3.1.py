# На вход подаётся число N - количество элементов в массиве numbers. Далее в N строках записаны целые числа  - элементы
# массива по порядку. В следующей строке идёт целое число target. Необходимо найти два числа из массива numbers, сумма
# которых равна target. В выводе необходимо записать индексы этих чисел в порядке возрастания через пробел.
# Предполагается, что в каждом тесте есть только одно решение. Также нельзя использовать один и тот же элемент дважды.
# Чтобы вернуть значение для ответа, можете использовать print
#
# The input is the number N - the number of elements in the numbers array. Next, N lines contain integers - the elements
# of the array in order. The next line contains the integer target. You need to find two numbers from the numbers array
# whose sum is equal to target. In the output you need to write the indices of these numbers in ascending order
# separated by a space.
# It is assumed that each test has only one solution. You also cannot use the same element twice.
# To return a value for the response, you can use print
# Sample Input:
#
# 4
# 2
# 7
# 11
# 15
# 9
# Sample Output:
# 0 1

def main():
    amount_of_elements = int(input("Input amount of elements\n"))
    array_with_elements = []
    for i in range(0, amount_of_elements):
        array_with_elements.append(int(input(f"Input  element (num of elements: {i + 1})\n")))
        
    expected_sum = int(input("Input expected sum\n"))

    for i in range(0, amount_of_elements):
        for y in range(i+1, amount_of_elements):
            if expected_sum == array_with_elements[i]+array_with_elements[y]:
                return i, y


if __name__ == "__main__":
    print(main())
