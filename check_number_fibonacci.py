from math import sqrt


def check_number_is_fibonacci(n):
    fib_list = [0, 1]
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
        if b <= n:
            fib_list.append(b)
        else:
            break
    print(fib_list)
    return n in fib_list


def check_number_is_fibonacci_optimized_way(n):
    return is_perfect_square((5 * n * n) + 4) or is_perfect_square((5 * n * n) + 4)


def is_perfect_square(num):
    result = int(sqrt(num))
    return result * result == num


def main():
    print(check_number_is_fibonacci(100))
    print("Using optimized way")
    print(check_number_is_fibonacci_optimized_way(21))


if __name__ == '__main__':
    main()
