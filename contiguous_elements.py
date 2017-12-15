#!/usr/bin/python3

def conti_elements(input_list, number):

    total = 0
    len_list = len(input_list) - 1
    ind = 0
    l = []
    j = 0
    while ind < len_list:
        total = input_list[ind] + input_list[ind + 1]
        if total == number:
            return input_list[ind:ind+2], total
        elif total > number:
            total = 0
        else:
            j = ind + 1
            if j < len_list:
                pass
            else:
                total += input_list[j + 1]
                if total == number:
                    j += 1
                    l.extend(input_list[ind:j + 1]) 
        ind += 1
    return l,total
def main():
    input_list = [6,5,3,2,1,7]
    number  = int(input("accept number"))
    #ele_list, total = conti_elements(input_list, number)
    #print("elements from list are {0}==>{1}".format(ele_list, total))
    
    len_list = len(input_list) - 1
    
    total = 0
    l = []
    j = 0
    for i in range(len_list):
        j = i + 1
        total = sum(input_list[i : j + 1])
        if total == number:
            print("{0}===>{1}".format(total,input_list[i : j + 1]))
        if total <  number:
            k = j + 1
            total += sum(input_list[k:k+1])
            if total == number:
                print("{0}===>{1}".format(total,input_list[i : k + 1]))

if __name__ == '__main__':
    main()
