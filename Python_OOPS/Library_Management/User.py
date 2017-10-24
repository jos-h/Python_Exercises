#!/usr/bin/python3
import Python_OOPS.Library_Management.Subscription


class User(object):

    __isSubscribed = None
    __monthly_subs = 0
    __weekly_subs = 0
    __yearly_subs = 0

    __user_dict = {}
    __user_id = 0

    def __init__(self, userName, Address, Age, Gender, contactNumber):
        self.__userName = userName
        self.__Address = Address
        self.__Age = Age
        self.__Gender = Gender
        self.__contactNumber = contactNumber

        self.__user_id += 1


    def setAddress(self, Address):
        self.__Address = Address
    

    def getAddress(self):
        return self.__Address


    def setContactNumber(self, contact_number):
        self.__contactNumber = contact_number


    def getContactNumber(self):
        return self.__contactNumber


    def getSubscription(self,choice):
        if choice == 'y':
            self.__isSubscribed = 1
        else:
            self.__isSubscribed = 0

        if self.__isSubscribed:

            subs = eval(input("Do u want yearly"+"\n"+"weekly"+"\n"+"montly"+"subscription"))

            if subs == "monthly":
                self.__monthly_subs = self.Subscription.getMonthlyPrice()
            elif subs == "weekly":
                self.__weekly_subs = self.Subscription.getWeeklyPrice()
            elif subs == "yearly":
                self.__yearly_subs = self.Subscription.getYearlyPrice()

