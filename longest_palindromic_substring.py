from pprint import pprint


def lps(s):
    n = len(s)
    max_len = 1
    table = [[0 for _ in range(n)] for _ in range(n)]

    # table of length 1
    i = 0
    while i < n:
        table[i][i] = 1
        i += 1

    # length 2
    start = i = 0
    while i < n - 1:
        if s[i] == s[i + 1]:
            table[i][i + 1] = 1
            start = i
            max_len = len(s[start:i + 2])
            print(max_len, s[start:i + 2])
        i += 1
    # length > 2
    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            # ending index of substring from
            # starting index i and length k
            j = i + k - 1
            if table[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = 1

                if k > max_len:
                    start = i
                    max_len = k
            i += 1
        k += 1

    pprint(table)
    print("longest substring is", s[start: start + max_len])
    print("max length", max_len)


def optimized_lps(s):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j - i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    print(m, len(m))


s = 'forgeeksskeegfor'
s = 'babad'
# lps(s)
optimized_lps(s)
