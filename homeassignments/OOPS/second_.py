class FirstClass(object):
    def setdata(self,value):
        self.data = value
        self.x = 10
    def display(self):
        print(self.data)


if __name__ =='__main__':
    o1 = FirstClass()
    o2 = FirstClass()
    o1.setdata(12)
    o1.display()
    o2.setdata(122)
    o2.display()
    print(o1.__dict__,o2.__dict__)
    print("class",FirstClass.__dict__)
