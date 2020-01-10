from _datetime import datetime


class ABC(object):
    a = 10

    def __new__(cls, *args, **kwargs):
        print("Overriding __new__ method")
        print("Args", args)
        print("Kwargs", kwargs)
        instance = super(ABC, cls).__new__(cls, *args, **kwargs)
        print("new", instance)
        return instance

    def __init__(self):
        print("constructor call")

    def method(self):
        print(self.a)
        return "instance method called", self

    @classmethod
    def class_method(cls):
        cls.a = 12
        return "class method called", cls, cls.a

    @staticmethod
    def static_method():
        return "static method called", ABC().a


def main():
    obj = ABC()
    print(obj.method())
    print("____________________________________")
    print(obj.class_method())
    print("____________________________________")
    print(obj.static_method())
    print("************************************")
    print(obj.method())

if __name__ == '__main__':
    main()
