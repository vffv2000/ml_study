#
# На вход подаётся целое число N. Далее вводятся N строк. Необходимо определить самый длинный общий префикс
# (т.е. определить самую длинную подстроку, с которой начинаются все данные строки).
#
# В выводе необходимо записать данный префикс. В случае, если общего префикса нет - вернуть строку nan.
#
#
#
# The input is an integer N. Next, N lines are entered. It is necessary to determine the longest common prefix
# (that is, determine the longest substring with which all given strings begin).
#
# This prefix must be written in the output. If there is no common prefix, return the string nan.

def main():
    amount_of_elements = int(input("Input amount of elements\n"))
    array_with_elements = []
    for i in range(0, amount_of_elements):
        array_with_elements.append(str(input(f"Input  element (num of elements: {i + 1})\n")))

    for y in range(1, len(min(array_with_elements)) + 1):
        for i in range(0, amount_of_elements):
            if array_with_elements[0][:y] != array_with_elements[i][:y]:
                if y == 1:
                    return 'nan'
                else:
                    return array_with_elements[0][:y - 1]


if __name__ == "__main__":
    print(main())
