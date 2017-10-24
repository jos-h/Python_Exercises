#!/usr/bin/python3


class Subscription(object):

    __monthly_Price = 100
    __weekly_price = 50
    __yearly_Price = 2000

    @staticmethod
    def getMonthlyPrice(self):
        return self.__Monthly_Price

    @staticmethod
    def getWeeklyPrice(self):
        return self.__weekly_price

    @staticmethod
    def getYearlyPrice(self):
        return self.__yearly_Price