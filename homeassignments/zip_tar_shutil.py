#!/usr/bin/python3

import shutil


def zip_tar_file():
    my_path = "/home/sudouser/Command_Line_demo/abc"

    # provide the base dir and the file name along with the full path and the "extension
    shutil.make_archive(my_path,"tar","/home/sudouser/Command_Line_demo/","abc.txt")


def main():
    zip_tar_file()

if __name__ == '__main__':
    main()