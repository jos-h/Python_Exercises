#!/usr/bin/python3


class Publisher(object):

    def __init__(self, name, address, contact_number):

        self.__name = name,
        self.__adddress = address
        self.__contactNumber = contact_number

    def __del__(self) :
        print("destroyed")

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPhoneNumber(self, contact_number):
        self.__contactNumber = contact_number

    def getPhoneNumber(self):
        return self.__contactNumber


