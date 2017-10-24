def longest_line_file(file_name):
    line_len = 0
    temp_line = ''
    file_handle = open(file_name,"r")
    temp = ''
    for line in file_handle:
        temp_line_len = len(line)

        if line_len < temp_line_len:
            line_len = temp_line_len
            temp = line
        elif line_len <= temp_line_len:
            temp_line = line
    return temp, temp_line


def main():
    print("Longest line is {}".format(longest_line_file("D:\\Ubuntu_BackUp\\untitled\\audio.conf")))

    print("alternate way")




if __name__ == '__main__':
    main()