#!/usr/bin/python3

import random


class BankAccount(object):

    def __init__(self, user_name, amount, acc_num):
        self.__name = user_name
        self.__amount = amount
        self.__acc_num = (user_name + str(acc_num))

    def withdraw_amount(self, amount):
        if amount < 0:
            print("Account is nill:")
        else:
            self.__amount -= amount
            return self.__amount

    def deposit_amount(self, amount):
        if amount <= 0 :
            self.__amount += amount
        else:
            self.__amount += amount
            return self.__amount

    @staticmethod
    def auto_generate_account_number():
        return int(((random.random())*10000000000))

    def display(self):
        print("{0} contains {1}".format(self.__acc_num, self.__amount))


def main():

    account_number = int(BankAccount.auto_generate_account_number())
    obj1 = BankAccount("ABC",int(25000), account_number)

    print("Amount withdrawn is :",obj1.withdraw_amount(1000))
    obj1.display()

    print("Amount desposited is:",obj1.deposit_amount(12000))
    obj1.display()

if __name__ == '__main__':
    main()
    
