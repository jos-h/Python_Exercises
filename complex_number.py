def menu():
    n1, n2 = '2+3i', '1+2i'  # input("Accept two complex numbers").split()
    choice = input("Which operation to perform?")
    if choice == '+':
        print(f'Addition of complex number is {add_complex_numbers(n1, n2)}')
    elif choice == '-':
        print(f'Subtraction of complex number is {sub_complex_numbers(n1, n2)}')
    elif choice == '*':
        print(f'multiplication of complex number is {multiply_complex_numbers(n1, n2)}')
    elif choice == '/':
        print(f'Subtraction of complex number is {sub_complex_numbers(n1, n2)}')


def add_complex_numbers(num1, num2):
    t = num1.split('+')
    t1 = num2.split('+')
    a, b, c, d = int(t[0]), int(t[1][0]), int(t1[0]), int(t1[1][0])
    real_part = a + c
    imaginary_part = b + d
    return str(real_part) + "+" + str(imaginary_part) + "i"


def sub_complex_numbers(num1, num2):
    t = num1.split('+')
    t1 = num2.split('+')
    a, b, c, d = int(t[0]), int(t[1][0]), int(t1[0]), int(t1[1][0])
    real_part = a - c
    imaginary_part = b - d
    return str(real_part) + "+" + str(imaginary_part) + "i"


def multiply_complex_numbers(num1, num2):
    t = num1.split("+")
    t1 = num2.split("+")
    a, b, c, d = int(t[0]), int(t[1][0]), int(t1[0]), int(t1[1][0])
    real_part = (a * c) - (b * d)
    imaginary_part = (a * d) + (b * c)
    return str(real_part) + "+" + str(imaginary_part) + "i"


def divide_complex_numbers(num1, num2):
    pass


def main():
    menu()


if __name__ == '__main__':
    main()
