#!/usr/bin/python3


class DecoratorDemo(object):
    @staticmethod
    def staticdemo():
        print("Static method")
    @classmethod
    def classdemo(cls):
       print(type(cls),id(cls))
       print("class method")

    def ObjectTest(self):
        print("invoked using object",type(self))


def main():
    DecoratorDemo.staticdemo()
    DecoratorDemo.classdemo()
    print(id(DecoratorDemo))
    print(type(DecoratorDemo))
    dd = DecoratorDemo()
    dd.ObjectTest()
    #print(DecoratorDemo.__dict__)
    dd.classdemo()
if __name__ == "__main__":
    main()
