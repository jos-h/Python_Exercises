#!/usr/bin/python3


def sort_list(list_3):

    key = 0
    i = 1
    j = 0
    while i < len(list_3):
        j = i - 1
        key = list_3[i]
        while j >= 0 and key < list_3[j]:
                list_3[j + 1] = list_3[j]
                j -= 1
        list_3[j + 1] = key
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