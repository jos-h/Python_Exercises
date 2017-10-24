
def number_clumps_array(array):

    len_array = array.__len__()
    i = 0
    count_number_clumps = 0
    clumps = []
    flag = 0
    j = 0
    while i < len_array:
        j = i + 1
        if j > len_array - 1:
            break;
        else:
            if array[i] == array[j]:
                count_number_clumps += 1
                clumps.append(array[i:j+1])
        i += 1
    return clumps, count_number_clumps


def main():

    array = [1,2,2,3,4,4]
    li_count = 0
    li_clumps = list()

    li_clumps, li_count = number_clumps_array(array)
    print(li_clumps)
    print("count",li_count)


if __name__ =='__main__':
    main()