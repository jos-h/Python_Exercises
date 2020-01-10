def ispalindrome(num):
    t = num
    r = 0
    while num != 0:
        r = (r * 10) + (num % 10)
        num //= 10
    if r == t:
        return r


def infinite_palindromes():
    num = 0
    while True:
        if ispalindrome(num):
            print("****************", num)
            i = (yield num)
            if i is not None:
                num = i
        num += 1


def main():
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        digits = len(str(i))
        if digits == 5:
            pal_gen.close()
        pal_gen.send(10 ** digits)


if __name__ == '__main__':
    main()
