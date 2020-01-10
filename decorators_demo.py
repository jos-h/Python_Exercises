def my_dec(func):
    def wrapper():
        print("In wrapper inside dec func")
        func()
        print("After the func is called")

    return wrapper


@my_dec
def foo():
    print("inside foo")


foo()


def second_deco(func):
    def wrapper(*args, **kwargs):
        print("%%%%%%%%%%%%%%%%%%")
        func(*args, **kwargs)
        print("###################")
    return wrapper


def first_deco(func):
    def wrapper(*args, **kwargs):
        print("###################")
        func(*args, **kwargs)
        print("%%%%%%%%%%%%%%%%%%%")
    return wrapper


@second_deco
@first_deco
def fun(msg):
    print(msg)

fun("HELLO KUNAL")