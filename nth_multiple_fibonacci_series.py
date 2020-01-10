"""
Python Program for nth multiple of a number in Fibonacci Series

Examples:-
        Input : k = 2, n = 3
        Output : 9
        3\'rd multiple of 2 in Fibonacci Series is 34
        which appears at position 9.

        Input  : k = 4, n = 5
        Output : 30
        5\'th multiple of 5 in Fibonacci Series is 832040
        which appears at position 30.

"""


def nth_multiple_number(n, k):
    a = 0
    b = 1
    i = 2
    while i != 0:
        a, b = b, a + b
        if b % k == 0:
            return n * i
        i += 1


def nth_multiple_number_formal_way(n, k):
    cnt = 0
    pos = 2
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        if b % k == 0:
            cnt += 1
        if cnt == n:
            return pos  # , b

        pos += 1


def test_answer():
    assert nth_multiple_number_formal_way(5, 4) == 30


def main():
    n = 8
    k = 4
    print(nth_multiple_number_formal_way(n, k))
    print("Optimized way")
    print(nth_multiple_number(n, k))


if __name__ == '__main__':
    main()
