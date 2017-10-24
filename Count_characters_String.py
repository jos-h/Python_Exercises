#!/usr/bin/python3


def character_count_string(input_string):

    count_dict = {}

    for s in input_string:

        keys = count_dict.keys()

        if s in keys:
            count_dict[s] += 1
        else:
            count_dict[s] = 1

    print(count_dict)


def main():

    s = str(input("accept string from user"))
    character_count_string(s)
if __name__ == '__main__':
    main()