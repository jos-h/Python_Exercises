#!/usr/bin/python3

import Python_OOPS.books

class libraryManager(object):

    __bookStock = 0
    __bookId = 0
    
    def __init__(self, libraryName, libraryAddress, libraryNumber):
        self.__libraryName = libraryName
        self.__libraryAddress = libraryAddress
        self.__libraryNumber = libraryNumber
        
    def setAddress(self, Address):
        self.__libraryAddress = Address

    def getAddress(self):
        return self.__libraryAddress

    def setPhoneNumber(self, phoeNumber):
        self.__libraryNumber = phoeNumber

    def getbookStocks(self, bookStock):
        self.__bookStock = bookStock
    
    def getBookId(self):
        return self.__bookId

    '''
        add books function
         bookId is autoincrement

    '''
    def addBooks(self):

        name = input("Accept the book Name")

        price = int(input("Accept the price of book"))

        authorName = input("Accept the name of the author")

        edition = input("Edition of book")

        bookId = self.getBookId + 1

        book_obj = Python_OOPS.books(bookId, name, price, authorName, edition)




        '''
            saving books information such as name, price etc in
            dictionary
        '''

        booksDict = dict() #{}

        booksDict[bookId] = book_obj

        self.view_books(booksDict)

    '''
        Display books information
    '''
    def view_books(self,books_dict):
        print(self.books_dict)

    '''
        Fucntion to issue book
        i/p :=> User Information
    '''
    def issueBook(self):

        userName = eval(input("May i know ur name?"))

        address = eval(input("Address"))

        age = int(input("Enter ur age"))

        gender = eval(input("Specify ur gender"))

        contact_number = int(input("Enter ur phone number"))

        user_obj = self.User(userName, address, age, gender, contact_number)

        book_name = eval(input("Book name"))

        for book_name in

        print("do u want subscription type y/n")
        choice = eval(input("Enter yes or no"))

        if choice == 'y':
            self.User.getSubscription(choice)

    def add_new_user(self):

        new_user_name = eval(input("Enter the name"))
        address = eval(input("enter address"))
        age = int(input("Enter your age"))
        gender = eval(input("Enter gender"))
        contact_number = int(input("Enter your contact number"))

        new_user_obj = self.User(new_user_name, address, age, gender, contact_number)


def menu():
    choice = 0
    while True:
        print("1:Add user")
        print("2:Add books")
        print("3:Display")
        print("4:display subscriped users")

        choice = int(input("Enter choice"))
        return choice


def main():
    choice = menu()

    '''
        Library Manager Object Creation
        Constructor call
    '''
    library_obj = libraryManager("DyanGanga Books Depot","A-44,Navajeevan Park,Hadapsar,Pune",+919762745422)

    '''
        Adding new User
    '''
    if choice == 1:
        library_obj.add_new_user()

if __name__ == '__main__':
    main()