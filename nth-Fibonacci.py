FIB_LIST = [0, 1]

def nth_fibonacci_number(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return nth_fibonacci_number(num - 1) + nth_fibonacci_number(num - 2)


def nth_fibonacci_dynamic_program(num):
    if num < 0:
        return "Incorrect Input"
    if num <= len(FIB_LIST):
        return FIB_LIST[num - 1]
    else:
        value = nth_fibonacci_number(num - 1) + nth_fibonacci_number(num - 2)
        FIB_LIST.append(value)
        return FIB_LIST[-1]


def main():
    a = 0
    b = 1
    l = [0, 1]
    for i in range(2, 100):
        a, b = b, a + b
        l.append(b)
    print(l)
    print(nth_fibonacci_number(9))

    print("Dynamic Programming")
    print(nth_fibonacci_dynamic_program(9))

    a = 0
    b = 1
    for i in range(2, 10):
        a, b = b, a + b
    print(b)

if __name__ == '__main__':
    main()
