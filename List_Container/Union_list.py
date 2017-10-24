#!/usr/bin/python3


def menu():
    print("1:Union of Lists\n"
          "2:Intersection of Lists\n"
          "3:Difference in Lists\n"
          "4:Exit")
    choice = eval(input("Accept the choice"))
    return choice


def union_lists(list_1, list_2):
    list_3 = []
    list_3.extend(list_1)

    for x in list_2:
        if x not in list_3:
            list_3.append(x)
    return list_3


def intersection_list(list_1, list_2):
    list_3 = []
    for x in list_1:
        for y in list_2:
            if x == y:
                list_3.append(x)
    return list_3


def difference_lists(list_1, list_2):
    list_3 = []
    j = 0;
    list_3.extend(list_1)
    while j < list_3.__len__():
        i = 0
        while i < list_2.__len__():
            if list_3[j] == list_2[i]:
                list_3.remove(j)
            i += 1
        j += 1
    return list_3


def main():
    list_1 = eval(input("Accept 1st list"))
    list_2 = eval(input("Accept 2nd list"))

    while True:
        choice = menu()
        if choice == 1:
            print("Union of list is {}".format(union_lists(list_1,list_2)))
        elif choice == 2:
            print("Intersection of list is {}".format(intersection_list(list_1, list_2)))
        elif choice == 3:
            print("Difference between lists is {}".format(difference_lists(list_1, list_2)))
        else:
            print("bye")
            return


if __name__ == "__main__":
    main()