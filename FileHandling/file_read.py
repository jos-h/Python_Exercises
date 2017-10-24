#!/usr/bin/python 3


def read_file():

    fd = open("/home/mastermind/untitled/google_assignments/pattern_menu.py", "r")

    return fd


if __name__ == "__main__":
    print(read_file().read())
