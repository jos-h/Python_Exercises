import weakref


class Car:

    def __init__(self, w):
        self.wheels = w


def main():
    obj = Car(5)
    print("obj memory location", hex(id(obj)))
    r = weakref.ref(obj)
    print("Before", r)
    obj = None
    print("After:", r)
    print("Garbage collected immediately")


if __name__ == '__main__':
    main()
