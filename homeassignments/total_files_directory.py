#!/usr/bin/python3

import os
from os import path
from os.path import isfile,isdir


def list_files_dir():

    path = "//home//sudouser//python"

    files = os.listdir(path)

    for f in files:
        if isfile(f):
            print(f)


def main():
    list_files_dir()



if __name__ =='__main__':
    main()