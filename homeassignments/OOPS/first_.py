class first_(object):

    '''def __init__(self):
        print("const")'''
    def __del__(self):
        print("destruct")


if __name__ == '__main__':
    t1 = first_()
    t1.x = 10
    print(t1.__dict__)
    print(t1.x)
