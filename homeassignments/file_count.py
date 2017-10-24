#!/usr/bin/python3

import os
from os import listdir
from os.path import isfile, isdir, join


def count_files():
    count = 0
    cnt = 0
    dir_cnt = 0
    my_path = "/home/sudouser/python"
    dir_ = os.listdir(my_path)
    for d in dir_:

        if isfile(join(my_path,d)):
            count += 1
        if isdir(d):
            dir_cnt += 1
    return count, dir_cnt


def main():
    file_count, dir_cnt = count_files()
    print("Count of files {} \nCount of directories {}".format(file_count, dir_cnt))


if __name__ == '__main__':
    main()
