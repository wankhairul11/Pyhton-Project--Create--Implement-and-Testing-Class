class Book:
    # Class variable to keep track of total number of books
    total_books = 0

    def __init__(self, title, author):
        # Instance variables
        self.title = title
        self.author = author
        
        # Increment the total number of books when a new book is created
        Book.total_books += 1

    def get_info(self):
        # Returns the title and author of the book
        return f"Title: {self.title}, Author: {self.author}"

    @classmethod
    def get_total_books(cls):
        # Returns a formatted string with the total number of books created
        return f"The total number of books is {cls.total_books}"

    @staticmethod
    def is_valid_title(title):
        # Checks if the title is a non-empty string
        return isinstance(title, str) and len(title) > 0

# Test script
if __name__ == "__main__":
    # Create two instances of Book
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")

    # Print the information of each book using the get_info method
    print(book1.get_info())  # Output: Title: To Kill a Mockingbird, Author: Harper Lee
    print(book2.get_info())  # Output: Title: 1984, Author: George Orwell

    # Use the static method to check if a book title is valid
    print(Book.is_valid_title("To Kill a Mockingbird"))  # Output: True
    print(Book.is_valid_title(""))  # Output: False
    print(Book.is_valid_title(123))  # Output: False

    # Print the total number of books created using the class method
    print(Book.get_total_books())  # Output: The total number of books is 2
