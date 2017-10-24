#!/usr/bin/python3


def get_products_of_all_ints_except_at_index(li):

    i = 0
    multiply_ans = 1
    temp_list = li

    products_of_all_ints = list()
    try:
        if li.__len__() < 2:
            raise IndexError
        else:
            while i < li.__len__():
                if i == 0:
                    prod = get_product_except_index(li[i + 1:])
                elif i >= 1:
                    li = temp_list[i-i:i] + temp_list[i+1:]
                    prod = get_product_except_index(li)
                i += 1
                products_of_all_ints.append(prod)
            return  products_of_all_ints

    except IndexError:
        print("We require 2 numbers to find product")


def get_product_except_index(li):

    i = 0
    prod = 1
    while i < li.__len__():
        prod *= li[i]
        i += 1
    return prod


def main():
    li = list()

    li = [1,7,3,4]

    print("====>",get_products_of_all_ints_except_at_index(li))


if __name__ == '__main__':
    main()