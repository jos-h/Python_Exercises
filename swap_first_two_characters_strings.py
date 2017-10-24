#!/usr/bin/python3


def swap_first_two_characters(first_str, second_str):

    temp_first = first_str[:2]
    temp_second = second_str[:2]

    second_str = second_str.replace(temp_second, temp_first)
    first_str = first_str.replace(temp_first, temp_second)

    return first_str + " " + second_str


def main():

    print("=====",swap_first_two_characters('abc','xyz'))

if __name__ == '__main__':
    main()