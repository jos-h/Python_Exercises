def merge_list(src_list, dest_list):
    
    src_list.extend(dest_list)
    src_list.sort()
    return src_list
    
def main():
    
    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]
    var = merge_list(my_list,alices_list)
    print("merged list is",var)

if __name__ == '__main__':
    main()
