class Book:
    def __init__(self, isbn="", title="", pages="", copies=0):
        self.isbnNumber = isbn
        self.title = title
        self.numPages = pages
        self.copies = copies
        #self.availableCount = avCount

    def __repr__(self):
        return "ISBN: {} \n title: {}\n pages: {}\n copies: {}\n".format(self.isbnNumber, self.title, self.numPages, self.copies)

    def getISBN(self):
        return self.isbnNumber

    def getTitle(self):
        return self.title

    def getPages(self):
        return self.numPages

    def getCopies(self):
        return self.copies

