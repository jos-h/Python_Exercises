"""
    Re-arranging the array elements even odd even or
    odd even odd on the min element from the list.

"""


def add_elements_array(new_list, array, index, counter):
    """

    :param new_list: list with all 0's
    :param array: list with even or odd numbers respectively
    :param index: position to insert
    :param counter: to increment with 2
    :return: list with numbers added odd even odd / even odd even ..
    """
    while index < len(array):
        new_list[counter] = array[index]
        index += 1
        counter += 2
    return new_list


def traditional_approach(input_list):
    """

    :param input_list: list with integers in it
    :return: does not return but prints new list
    """
    flag = 0
    odd_list = []
    even_list = []
    new_list = [0 for _ in range(len(input_list))]
    if input_list[0] % 2 == 0:
        flag = 1

    for each_number in input_list:
        if each_number % 2 == 0:
            even_list.append(each_number)
        else:
            odd_list.append(each_number)

    if flag == 1:
        new_list = add_elements_array(new_list, even_list, 0, 0)
        new_list = add_elements_array(new_list, odd_list, 0, 1)
    elif flag == 0:
        new_list = add_elements_array(new_list, odd_list, 0, 0)
        new_list = add_elements_array(new_list, even_list, 0, 1)
    print(new_list)


def pythonic_way(input_list):
    """

    :param input_list:
        list of integers
    """
    flag = 1 if min(input_list) % 2 == 0 else 0
    new_list = [0] * len(input_list)
    even_list = list(filter(lambda x: x if x % 2 == 0 else False, input_list))
    odd_list = list(filter(lambda x: x if x % 2 != 0 else False, input_list))
    if flag == 1:
        new_list[::2] = even_list
        new_list[1::2] = odd_list
    else:
        new_list[::2] = odd_list
        new_list[1::2] = even_list

    print(new_list)


def main():
    """
    Does not return but prints the list
    :return:
    """
    input_list = [9, 12, 23, 8, 5]
    input_list = [47, 49, 36, 98, 90]
    input_list.sort()
    traditional_approach(input_list)
    # input_list.sort()
    # flag = 0
    # odd_list = []
    # even_list = []
    # new_list = [0 for _ in range(len(input_list))]
    # if input_list[0] % 2 == 0:
    #     flag = 1
    #
    # for each_number in input_list:
    #     if each_number % 2 == 0:
    #         even_list.append(each_number)
    #     else:
    #         odd_list.append(each_number)
    #
    # if flag == 1:
    #     new_list = add_elements_array(new_list, even_list, 0, 0)
    #     new_list = add_elements_array(new_list, odd_list, 0, 1)
    # elif flag == 0:
    #     new_list = add_elements_array(new_list, odd_list, 0, 0)
    #     new_list = add_elements_array(new_list, even_list, 0, 1)
    # print(new_list)

    print("********************************")
    print("Pythonic Approach")
    pythonic_way(input_list)
    print("********************************")


if __name__ == '__main__':
    main()
