# На вход подаётся целое число x. Необходимо вывести true, если число x является палиндромом, false - если
# не является палиндромом.
#
# The input is an integer x. It is necessary to output true if the number x is a palindrome,
# false - if it is not a palindrome.

def main():
    palindrome = str(input("Input palindrome\n"))
    revers_palindrome=palindrome[::-1]
    if palindrome == revers_palindrome:
        return True
    else:
        return False


if __name__ == "__main__":
    print(main())
