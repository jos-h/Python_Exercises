#!/usr/bin/python

class complex_number(object):

    def __init__(self,real_part, imaginary_part):
        self.real_no = real_part
        self.imag_no = imaginary_part

    def display(self):
        print(self.real_no+"+"+self.imag_no)

    def add_complex(self, real_no, real_no_2, imag_no, imag_no_2):
        real_part = str((int(self.real_no) + int(real_no_2)))
        imag_part = str((int(self.imag_no) + int(imag_no_2))) + "i"

        return str(real_part)+"+"+str(imag_part)

    def sub_complex(self, real_no, real_no_2, imag_no, imag_no_2):
        real_part = str(int(self.real_no) - int(real_no_2))
        imag_part = str(int(self.imag_no) - int(imag_no_2)) + "i"

        return str(real_part) + "+" + str(imag_part)

    def add_only_complex_part(self, real_no, imag_no, real_no_2):

        return str(int(self.real_no) + int(real_no_2)) + "+" + str(imag_no+"i")

    def sub_only_complex_part(self, real_no, imag_no, real_no_2):

        return str(int(self.real_no) - int(real_no_2)) + "+" + str(imag_no+"i")

    def multiply_complex(self, real_no, imag_no, real_no_2, imag_no_2):

        num = imag_no + "i"
        num_2 = real_no_2 + "+" + (imag_no_2 + "i")

        print("*********",int(self.real_no) * int(num_2))
        product = ( int(self.real_no) * int(num_2) ) + ( int(num) * int(num_2) )
        return product
    
    def __del__(self):
        print("bye")

def main():

         real_no = eval(input("Enter the real part"))
         imag_no = eval(input("Enter the imaginary part"))

         obj_1 = complex_number(real_no, imag_no)
         obj_1.display()

         add = obj_1.add_complex(real_no, eval(input("Enter the real part")), imag_no, eval(input("Enter the imaginary part")))
         print("Addition is =>", add)

         #sub = obj_1.sub_complex(real_no, eval(input("Enter the real part")), imag_no, eval(input("Enter the imaginary part")))
         #print("Subtraction is =>", sub)

         #print("==>",obj_1.add_only_complex_part(real_no, imag_no, eval(input("Enter the real part"))))

         #print("==>", obj_1.sub_only_complex_part(real_no, imag_no, eval(input("Enter the real part"))))

         print("==>", obj_1.multiply_complex(real_no, imag_no,eval(input("Enter the real part")),eval(input("Enter the imag part"))))


if __name__ == '__main__':
    main()
