#!/usr/bin/python3


def add_ing_at_end_ly(str):

    if str.__len__() < 3:
        return "len must be greater than or equal to 3"
    elif str.__len__() >= 3:
        if str.endswith('ing'):
            return str + 'ly'
        elif 'ing' not in str:
            return str + 'ing'


def main():

    print("string is",add_ing_at_end_ly('st'))


if __name__ == '__main__':
    main()