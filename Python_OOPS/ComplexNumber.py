#!/usr/bin/python3


class ComplexNumber:

    def __init__(self, real, imag):
        '''
        :param real:
        :param imag:
         constructor is invoked when the object is created
         Constructor is not overloaded in python as it is a runtime language
         We can either write a default / parameterized constructor
        '''
        self.__real = real
        self.__imag = imag

    def __del__(self):
        '''
        destructor is used to free the resources allocated inside the constructor
        :return:
        '''
        
    def __add__(self,c2):
        '''
        this method is invoked when we add 2 complex objects
        c1 + c2
        at this time the + invokes the __add__() method
        :param c2:
        :return: sum of the 2 complex numbers
        '''
        result = ComplexNumber(0,0)
        if isinstance(c2 , int):
            result.__real = self.__real + c2
        elif isinstance(c2, ComplexNumber):
            result.__real = self.__real + c2.__real
            result.__imag = self.__imag + c2.__imag
        return str(result.__real) + "+" + ( str(result.__imag) + "i" )

    def __sub__(self,c2):
        '''
        this method is invoked when we sub 2 comples numbers c1 - c2
        OR
        when we are subtracting an interger from complex number
        :param c2:
        :return: diff of 2 complex numbers OR diff of integer with the real part from complex number
        '''

        result = ComplexNumber(0,0)
        if isinstance(c2, int):
            result.__real = self.real - c2
        elif isinstance(c2, ComplexNumber):
            result.__real = self.__real + c2.__real
            result.__imag = self.__imag + c2.__imag
        return str(result.__real) + "-" + (str(result.__imag) + "i" )


def menu():

    choice = 0
    while True:

        print("1:Add 2 complex numbers")
        print("2:Add integer to complex numbers")
        print("3:Sub 2 complex numbers")
        print("4:Sub integer from complex numbers")
        print("5:Multiply an integer to complex numbers")
        print("6:Exit")

        choice = int(eval(input("Accept choice")))
        return choice


def main():

    choice = menu()
    while choice != 6:
        if choice == 1:
            real, imag = eval(input("Accept the real and the imag number"))
            c1 = ComplexNumber(real, imag)
            real, imag = eval(input("Accept the real and the imag number"))
            c2 = ComplexNumber(real, imag)
            result = c1 + c2
            print("+=>",result)
        if choice == 2:
            real, imag = eval(input("Accept the real and the imag number"))
            c1 = ComplexNumber(real, imag)
            real, imag = eval(input("Accept the real and the imag number"))
            c2 = ComplexNumber(real, imag)
            result = c1 - c2
            print("+=>", result)

if __name__ == "__main__":
    main()
