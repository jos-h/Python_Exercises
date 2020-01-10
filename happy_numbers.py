def square_num(num, ans):
    while num:
        ans = ans + (num % 10) * (num % 10)
        num //= 10
    return ans


# s = f = num
# while True:
#     s = square_num(s)
#     f = square_num(square_num(f))
#     print("======", s)
#     print("______", f)
#     if s != f:
#         continue
#     else:
#         break

def main():
    num = int(input("Accept numbers"))
    ans = 0
    t = num
    while True:
        s = square_num(t, ans)
        if s != 1:
            t = s
            print(s)
        else:
            break
    print(f"{num} is Happy number")


if __name__ == '__main__':
    main()
