# LibraryCatalog
The program is implemented to manage books, users and their relationships.


 ## Requirements ##
  * Create a book class with a title, page count, ISBN and whether or not it is checked out or not. 
  * Manage a collection of various books and allow the user to check out books or return books. 
  * Allow to generate a report of those books overdue and any fees. Also allow users to put books on reserve.
  * Books are stored in a File with following format:


     [ISBN number]       |[0156012197]      
     --------------------|-------------------------
    title=               |title = The Little Prince
    pages=               |pages = 93
    count=               |copies = 4
    available_count=     |available_copies = 1

  * Users are stored in a File with following format:

    [user id number]     |[1234]     
     --------------------|-------------------------
    name= name surname   |name = John Doe 
  
  
  ### Functional Specifications ###
- [x] User checkout book
    - Allow user to checkout a book. The value of available copies of the book should
    be reduced. Save the time of check-out to further check if the book is overdue
    and compute the fine.
- [x] User return book
    - Allow user to return a book. The value of available copies of the book should be
    increased.
- [x] User reserve book (subscribe)
    - Allow user to put a book in reserve if it is not available
- [x] Get subscribers of the book
    - Get the list of users that have put the book on reserve
- [x] Get notifications for reserved books
    - Get list of books that have been reserved by user and became available
recently. The notification is shown only once after book becomes available, after
displaying the notification it is deleted
- [ ] Get overdue books of the user
    - Get list of books that are overdue (more than 3 months checked out by the
user)
- [ ] Get fine for overdue book of the user
    - Get fine for the given book (5$ each week overdue) for the user
- [ ] Get total fine
    - Get total fine for all the overdue books of the user
- [x] Check book is available
    - Check if available copy of book is present
- [x] Get users who checked out book
    - Get list of users that have checked out given book
- [x] Add user
    - Add user info to the LibraryCatalog, so that it’s saved in Users info file in same
format as others. Get info from standard input.
- [x] Add book (get info from standard input)
    - Add book info to the LibraryCatalog, so that it’s saved in Books info file in same
format as others. Get info from standard input.
- [x] Remove user
    - Remove user info to the LibraryCatalog, so that it’s removed form Users info
file.
- [x] Remove book
    - Remove book info to the LibraryCatalog, so that it’s removed form Users info
file.
