class demoClass(object):
    religion = "humanity"
   
    def __init__(self,name,address):
       self.name = name
       self.address = address
       self.__marks = 53

    def __del__(self):
       print("done")
#       print(self.__marks)

    def __display(self):
       print(self.name,self.address,self.__marks)

if __name__ == '__main__':
    h1 = demoClass("kunal","Pune")
    print(h1)
    h2 = demoClass("jamdade","pune")
    print(h2)
    print(h1.__dict__)
    print(demoClass.__dict__)
    h1.teach = True
    print(h1.__dict__)
    print(h2.__dict__)
    #print(h1._demoClass__marks)
    h1.__display()
    h1._demoClass__display()
