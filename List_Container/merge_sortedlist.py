#!/usr/bin/python3


def merge_list(list_1, list_2):
    list_3 = list()     # OR list_3 = []  Creating new list
    i = 0;j = 0
    while i < list_1.__len__() and j < list_2.__len__():
        if list_1[i] < list_2[j]:
            list_3.append(list_1[i])
            i += 1
        else:
            list_3.append(list_2[j])
            j += 1

    if i < list_1.__len__():
        list_3.extend(list_1[i:])
    elif j < list_2.__len__():
        list_3.extend(list_2[j:])

    return list_3


def main():
    list_1 = eval(input("accept the first list"))
    list_2 = eval(input("accept the second list"))
    print("merge list is {}".format(merge_list(list_1, list_2)))



if __name__ == '__main__':
    main()