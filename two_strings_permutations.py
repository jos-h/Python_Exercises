#!/usr/bin/python3


def two_strings_permutation(first_str, second_str):
    if first_str.__len__() != second_str.__len__():
        return False
    return sorted(first_str) == sorted(second_str)


def main():

    first_str = str(input("Accept the first string"))
    second_str = str(input("Accept the second string"))

    permut = two_strings_permutation(first_str, second_str)

    if permut:
        print("{0} is permutation of {1}".format(first_str, second_str))
    else:
        print("{0} is not a permutation of {1}".format(first_str, second_str))


if __name__ == '__main__':
    main()