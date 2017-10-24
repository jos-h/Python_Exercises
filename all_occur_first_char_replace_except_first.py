#!/usr/bin/python3


def replace_occurrences_first_char_except_first(replace_str):

    first_char = replace_str[0]
    replace_str = replace_str.replace(first_char, '$')
    return(first_char + replace_str[1:])


def main():
    print(replace_occurrences_first_char_except_first("restart"))
if __name__ == '__main__':
    main()