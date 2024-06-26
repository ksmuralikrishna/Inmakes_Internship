'''Task 32
You are working on a project to develop a class representing a Book. The Book
class should have properties such as title, author, and year of publication.
Implement the constructor for the Book class that initializes these properties
when a new Book object is created. Additionally, provide a method called
getBookInfo() that returns a string with the book's details in the format "Title:
[title], Author: [author], Year: [year]".
Write the constructor and the getBookInfo() method for the Book class'''


class Book:
    def __init__(self, title, author, yop):
        self.title = title
        self.author = author
        self.yop = yop
    
    def getBookInfo(self):
        return f"Title : {self.title}\nAuthor : {self.author}\nYear : {self.yop}"

book1 = Book("alchemist", "poulo cohelo", 1999)
print(book1.getBookInfo())