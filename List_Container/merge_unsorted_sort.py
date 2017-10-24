#!/usr/bin/python3


def sort_list(list_3):
    i = 0;j = 0
    swap = 0

    while i < list_3.__len__():
        j = i
        while j < list_3.__len__() - 1:
            if list_3[i] > list_3[j + 1]:
                swap = list_3[i];
                list_3[i] = list_3[j + 1]
                list_3[j + 1] = swap
            j += 1
        i += 1
    return list_3


def main():
    list_1 = eval(input("accept the first list"))
    list_2 = eval(input("accept the second list"))
    list_3 = []
    list_3.extend(list_1)
    list_3.extend(list_2)
    print("Merged list is {}".format(list_3))
    print("sorted list is {}".format(sort_list(list_3)))

if __name__ == '__main__':
    main()