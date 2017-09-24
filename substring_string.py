"""
Given two strings s1, s2, write a function that returns true if s2 is a special substring s1.
A special substring s2 is such that the s1 contains s2
where each character in s2 appears in sequence in s1,
but there can be any characters in s1 in between the sequence.

Example:

isSpecialSubstring('abcdefg', 'abc') => true
isSpecialSubstring('abcdefg', 'acg') => true
isSpecialSubstring('abcdefg', 'acb') => false;


The first two are abc and acg appears in 'abcdefg' in that order, although there might be multiple chars between the next character in s2.

The last one is false, because in 'acb' the character 'b' appears before the character 'c' in 'abcdefg'
"""


def check_dest(dest):
    des_len = len(dest) - 1
    i = 0
    j = 0
    while i < des_len and j <= des_len:
        j = i + 1
        if dest[i] > dest[j]:
            return False
        i += 1


def is_special_substring(org, dest):
    dest_len = len(dest)
    flag = 0
    val = check_dest(dest)

    if val == False:
        return False
    else:
        for j in dest:
            for i in org:
                if j == i:
                    flag += 1
                    break
    if flag == 3:
        return True


def main():
    val = is_special_substring('abcdefg', 'bad')

    if val:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    main()
