#!/usr/bin/python3


def len_list(list):
    list_len = 0
    for y in list:
        list_len += 1
    return list_len


def main():
    list = eval(input("Accept the list"))
    print("len of list is {}".format(len_list(list)))


if __name__ == '__main__':
    main()