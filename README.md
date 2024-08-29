Book Class Project

Overview
---------
This project implements a `Book` class in Python to manage and keep track of 
books. The `Book` class includes features for tracking the number of books 
created, checking the validity of book titles, and providing information about 
each book.

Features
--------
- Instance Variables:
  - `title` (string): The title of the book.
  - `author` (string): The author of the book.

- Class Variable:
  - `total_books` (integer): A counter to keep track of the total number of 
    books created.

- Methods:
  - `__init__(self, title, author)`: Initializes the book with the provided 
    title and author. Increments the `total_books` class variable by 1 each 
    time a new book is created.
  - `get_info(self)`: Returns a string containing the title and author of the 
    book.
  - `get_total_books(cls)`: Class method that returns a formatted string with 
    the total number of books created.
  - `is_valid_title(title)`: Static method that returns `True` if the title 
    is a non-empty string; otherwise, returns `False`.

Usage
------
Creating Book Instances
-----------------------
To create instances of the `Book` class, simply initialize with a title and 
an author:

  book1 = Book("To Kill a Mockingbird", "Harper Lee")
  book2 = Book("1984", "George Orwell")

Getting Book Information
------------------------
Retrieve the information of each book using the `get_info` method:

  print(book1.get_info())  # Output: Title: To Kill a Mockingbird, Author: 
                            Harper Lee
  print(book2.get_info())  # Output: Title: 1984, Author: George Orwell

Checking Title Validity
-----------------------
Use the static method `is_valid_title` to check if a book title is valid:

  print(Book.is_valid_title("To Kill a Mockingbird"))  # Output: True
  print(Book.is_valid_title(""))  # Output: False
  print(Book.is_valid_title(123))  # Output: False

Getting Total Number of Books
------------------------------
Get the total number of books created with the `get_total_books` class method:

  print(Book.get_total_books())  # Output: The total number of books is 2

Testing
-------
The provided test script demonstrates how to create book instances, retrieve 
book information, validate titles, and check the total number of books. To run 
the tests, execute the script and observe the outputs.

Contribution
-------------
Feel free to contribute to this project by submitting issues or pull requests.
