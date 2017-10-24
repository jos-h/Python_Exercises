#!/usr/bin/python3

import random

class Person(object):

    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    def __del__(self):
        print("destructor")

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getAge(self):
        return self.__age

class Employee(Person):
    
    records = dict()  # or {}
    main_dict = {}

    def __init__(self, name, address, age, department, designation):
        super(Employee, self).__init__(name, address, age)
        self.__department = department
        self.__designation = designation

    def __del__(self):
        print("Employe object destroyed")
    
    @staticmethod
    def get_auto_emp_number():
        return int(random.random() * 10000)


    def addEmployee(self, emp_num):
        self.records["emp_id"] = emp_num
        self.records["name"] = super(Employee, self).getName()
        self.records["address"] = super(Employee, self).getAddress()
        self.records["age"] = super(Employee, self).getAge()
        self.records["department"] = self.__department
        self.records["designation"] = self.__designation
        self.main_dict[self.records["emp_id"]] = self.records

    def display(self):
        for key, values in self.main_dict.items():
            print("{} => {}".format(key, values))


    def update_Emp_Record(self, update_name, update_desig, update_dept):
        if update_name != '':
            self.records['name'] = update_name
        if update_desig != '':
            self.records['designation'] = update_desig
        if update_dept != '':
            self.records['department'] = update_dept

def menu():
    choice = 0
    while True:
        print("1: Add an employee:")
        print("2: Display")
        print("3: Update record:")
        print("4: Delete record:")
        print("5: search record:")
        print("6: exit")
        choice = int(input("Accept the choice:"))
        return choice


def main():
    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter the name:\t")
            address = input("Enter address:\t")
            age = int(input("Enter age:\t"))
            department = input("Enter the department:\t")
            designation = input("Enter designation:\t")
            emp = Employee(name, address, age, department, designation)
            emp_number = Employee.get_auto_emp_number()
            emp.addEmployee(emp_number)
        elif choice == 2:
            emp.display()
        elif choice == 3:
            update_name = eval(input("Enter name to update"))

            ch = int(input("Do you want to update designation:(1/0)\t"))
            if ch == 1:
                update_desig = eval(input("Enter designation to update"))
            else:
                update_desig = ''
            ch = int(input("Do you want to update department:(1/0)\t"))

            if ch == 1:
                update_dept = eval(input("Enter department to update"))
            else:
                update_dept = ''

            emp.update_Emp_Record(update_name, update_desig, update_dept)
            emp.display()
        elif choice == 4:
            name = eval(input("Enter name to delete"))


if __name__ == "__main__":
    main()
