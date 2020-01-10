def infinite(int_range):
    num = 0
    while num <= int_range:
        yield num
        num += 1


l = (i ** 2 for i in infinite(1000))

print(l.__next__())
