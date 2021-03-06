import io
import sys
from datetime import datetime, timedelta
import configparser
from Book import Book


def isFileExists(fileName):
    try:
        with open(fileName, 'r') as file:
            return True
    except FileExistsError:
        return False


class User:
    def __init__(self, id, name):
        self.idNumber = id
        self.nameSurname = name

    def getId(self):
        return self.idNumber

    def getName(self):
        return self.nameSurname

    def __repr__(self):
        return "User id: {} name: {}".format(self.idNumber, self.nameSurname)


class LibraryCatalog:
    def __init__(self, userFileName="userFile.txt", bookFileName="bookFile.txt"):
        self.userArray = []
        self.booksArray = []
        self.availableCopies = {}
        self.bookToUserId = {}
        self.userIdToTime = {}
        self.bookSubscribers = {}
        if isFileExists(userFileName):
            self.readUsers(userFileName)
        if isFileExists(bookFileName):
            self.readBooks(bookFileName)
        self.userFileName = userFileName
        self.bookFileName = bookFileName

    def readUsers(self, userFileName):
        if userFileName:
            cp = configparser.ConfigParser()
            cp.read(userFileName)
            for userId in cp.sections():
                self.userArray.append(User(userId, cp.get(userId, "name")))

    def readBooks(self, bookFileName):
        if bookFileName:
            cp = configparser.ConfigParser()
            cp.read(bookFileName)
            for isbn in cp.sections():
                self.booksArray.append(
                    (Book(isbn, cp.get(isbn, "title"), cp.get(isbn, "pages"), cp.get(isbn, "copies"))))
                self.availableCopies[cp.get(isbn, "title")] = int(cp.get(isbn, "available_copies"))

    def checkoutBook(self, bookName, userId):
        if self.availableCopies[bookName] == 0:
            self.subscribe(bookName, userId)
            return
        self.availableCopies[bookName] -= 1
        if bookName not in self.bookToUserId:
            self.bookToUserId[bookName] = [userId]
            self.userIdToTime[userId] = [(bookName, datetime.date().today())]
        else:
            self.bookToUserId[bookName].append(userId)
            self.userIdToTime[userId].append((datetime.date().today()))

    def returnBook(self, bookName, userId):
        self.availableCopies[bookName] += 1
        del (self.bookToUserId[bookName])
        for item in self.userIdToTime[userId]:
            if item[0] == bookName:
                del (self.userIdToTime[userId][item])

        if bookName in self.bookSubscribers:
            self.checkoutBook(bookName, self.bookSubscribers[bookName][0])
            self.bookSubscribers[bookName].pop(0)


    def subscribe(self, bookName, userId):
        # Allow user to put a book in reserve if it is not available
        if bookName not in self.bookSubscribers:
            self.bookSubscribers[bookName] = [userId]
        else:
            self.bookSubscribers[bookName].append(userId)

    def getSubscribers(self, bookName):
        # Get the list of users that have put the book on reserve
        if bookName not in self.bookSubscribers:
            return None
        return self.bookSubscribers[bookName]

    def getUserOverdueBooks(self, userId):
        result = []
        for item in self.userIdToTime[userId]:
            if (datetime.date().today() - item[1]).month > 3:
                result.append(item[0])
        return result
        # Get list of books that are overdue(more than 3 months checked out by the user)

    def getFineForUser(self, bookName, userId):
        # Get total fine for all the overdue books of the user
        result = 0
        for item in self.userIdToTime[userId]:
            if item[0] == bookName:
                if (datetime.date().today() - item[1]).month > 3:
                    delta = (datetime.date().today() - item[1]) - timedelta(days=90)
                    result += 5 * (delta.days / 7)
                    break
        return result

    def getTotalFine(self, userId):
        # Get total fine for all the overdue books of the user
        result = 0
        for bookDatePair in self.userIdToTime[userId]:
            for item in bookDatePair:
                if (datetime.date().today() - item[1]).month > 3:
                    delta = (datetime.date().today() - item[1]) - timedelta(days=90)
                    result += 5 * (delta.days / 7)
        return result

    def isBookAvailable(self, bookName):
        if bookName not in self.availableCopies:
            return False
        return self.availableCopies.get(bookName) > 0

    def getCheckedOutUsers(self, bookName):
        if bookName not in self.bookToUserId:
            return None
        self.bookToUserId[bookName]

    def removeUser(self, userId):
        self.userArray = [user for user in self.userArray if user.getId() != userId]
        for book in self.bookSubscribers:
            if userId in self.bookSubscribers[book]:
                self.bookSubscribers[book] = [user for user in self.bookSubscribers[book] if userId != user]

        cp = configparser.ConfigParser()
        with open(self.userFileName, 'r') as fh:
            cp.readfp(fh)
        cp.remove_section(userId)
        with open(self.userFileNamee, 'w') as fh:
            cp.write(fh)

    def addUser(self):
        try:
            userId = int(input("user Id: "))
        except ValueError:
            userId = 0
            pass
        userName = input("user name")

        self.userArray.append(User(userId, userName))
        with open(self.userFileName, "a") as userFile:
            userFile.write("\n[{}]\nname = {}".format(userId, userName))

    def removeBook(self, bookName):
        sectionName = ""
        for book in self.booksArray:
            if book.getTitle() == bookName:
                sectionName = book.getISBN()
                break
        if bookName in self.bookToUserId:
            userId = self.bookToUserId[bookName]
            for item in self.userIdToTime[userId]:
                if item[0] == bookName:
                    del (self.userIdToTime[userId][item])
            del (self.bookToUserId[bookName])

        if bookName in self.bookSubscribers:
            del (self.bookSubscribers[bookName])
        self.booksArray = [book for book in self.booksArray if book.getTitle() != bookName]

        cp = configparser.ConfigParser()
        with open(self.bookFileName, 'r') as fh:
            cp.readfp(fh)
        cp.remove_section(sectionName)
        with open(self.bookFileName, 'w') as fh:
            cp.write(fh)

    def addBook(self):
        isbn = input("isbn: ")
        title = input("title: ")
        try:
            pages = int(input("pages: "))
        except ValueError:
            pages = 0
            pass
        try:
            count = int(input("count: "))
        except ValueError:
            count = 0
            pass
        try:
            available_count = int(input("available: "))
        except ValueError:
            available_count = 0
            pass

        self.booksArray.append(Book(isbn, title, pages, count))
        self.availableCopies[title] = available_count
        with open(self.bookFileName, "a") as booksFile:
            booksFile.write(
                "\n[{}]\ntitle = {}\npages = {}\navailable_copies = {}\navailable_copies = {}".format(isbn, title,
                                                                                                      pages, count,
                                                                                                      available_count))
