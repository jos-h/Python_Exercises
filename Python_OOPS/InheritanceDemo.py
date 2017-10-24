#!/usr/bin/python3

class Shape(object):
    def __init__(self):
        print("in Base class Constructor:")
    def __del__(self):
        print("in Base class Destructor:")
    def draw(self):
        pass
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.__radius = radius
    def draw(self):
        print("Radius of circle is {}".format(self.__radius))
    def area(self):
        return ((22//7) *((self.__radius) ** 2))

class Square(Shape):
    def __init__(self, length):
        self.__length = length
    def draw(self):
        print("Lenght of square is {}".format(self.__length))
    def area(self):
        return (self.__length) ** 2


def main():
    
    circle = Circle(int(input("Enter radius")))
    circle.draw()
    print("Area of circle {}".format(circle.area()))
    square = Square(int(input("Enter length")))
    square.draw()
    print("Area of sqaure {}".format(square.area()))


if __name__ == '__main__':
    main()
