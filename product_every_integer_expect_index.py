#!/usr/bin/python3


def get_products_of_all_ints_except_at_index(li):

    i = 0
    j = 0
    multiply_prod = 1
    len_list = li.__len__() - 1

    new_list = list()

    if li.__len__() <= 1:
        raise IndexError("Need at least 2 elements to find product of every "
                         "integer except at that index")

    while i <= len_list:
        if i == 0:
            temp = li[i+1:]
            product = calculate_product_list(temp)
            new_list.append(product)

        elif i >= 1:

            if i == len_list:
                new_product = calculate_product_list(li[:i])
                new_list.append(new_product)

            else:
                t1 = li[i-1:i]
                t2 = li[i+1:]
                t = t1 + t2
                #j = 0
                new_product = calculate_product_list(t)

                new_list.append(new_product)
        i += 1
    return new_list


def calculate_product_list(li):
    j = 0
    multiply_prod = 1
    while j < (len(li)):
        multiply_prod = multiply_prod * li[j]
        j += 1
    return multiply_prod


def main():
    li = list()
    li = [1,7,3,4]

    print("======>",get_products_of_all_ints_except_at_index(li))

if __name__ == '__main__':
    main()