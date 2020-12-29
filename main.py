import configparser
import io
import sys
from Book import Book
from LibraryCatalog import LibraryCatalog

if __name__ == "__main__":
    catalog = LibraryCatalog(userFileName="userFile.txt", bookFileName="booksFile.txt")
    catalog.removeBook("NorU")
    catalog.removeUser(123456)
    #catalog.addBook()
    #catalog.addUser()
    catalog.checkoutBook("The Count of Monte Cristo", 1)
    catalog.checkoutBook("The Count of Monte Cristo", 2)

