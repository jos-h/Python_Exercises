

def largest_block_string(s):
    j = 1
    cnt = 1
    max = 0
    len_s = len(s)
    i = 0
    sub_string = ' '
    sub_str = ' '
    while i < len_s:
        #cnt = 1
        j = i + 1
        if j > (len_s - 1):
            break;
        #max = cnt
        if s[i] == s[j]:
            cnt += 1

            if max < cnt:
                max = cnt;
            elif max == cnt:
                max_one = cnt

        else:
            cnt = 1

        i += 1
    print("Cnt is===>{}".format(max))
    print("The next highest length is =====>",max_one)


def main():
    largest_block_string("aabbcccBBBdddddd")


if __name__ == '__main__':
    main()