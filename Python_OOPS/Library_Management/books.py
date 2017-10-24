#!/usr/bin/python3


class books(object):

    __isAvailable = False

    def __init__(self, bookId, name, price, authorName, edition):
        self.__bookId = bookId
        self.__name = name
        self.__price = price
        self.__authorName = authorName
        self.__edition = edition

    def __del__(self):
        print("destroyed")

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setStatus(self, isAvailable):
        self.__isAvailable = isAvailable

    def getStatus(self):
        return self.__isAvailable

