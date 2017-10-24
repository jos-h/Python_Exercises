def fibonacci(lb, ub):
    f1 = 0
    f2 = 1
    ans = 0
    while lb <= ub:
        ans = f1 + f2
        f1 = f2
        f2 = ans
        lb += 1
        print(ans)


def main():
    lb = eval(input("accept the lower bound"))
    ub = eval(input("accept the higher bound"))
    print("fibonacci series is {}".format(fibonacci(lb, ub)))

if __name__ == '__main__':
    main()