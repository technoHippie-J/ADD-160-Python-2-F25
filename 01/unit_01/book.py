"""

Objective
    Students will create a Book class with specified attributes and methods, instantiate three objects of this class and print out their details and length status. The completed program should be uploaded to your ADD 160 directory on GitHub, and the link should be submitted.

Steps to Complete the Assignment
1. Create the Book Class:
    - Define a class named Book.
    - Inside the class, create an __init__ method with three parameters: title, author, and pages.
    - Initialize these parameters as attributes of the class.
2. Add Methods to the Book Class:
    - Create a method display_details that prints the title, author, and pages of the book.
    - Create a method is_long_book that returns True if the book has more than 100 pages, otherwise returns False.
3. Create Instances of the Book Class:
    - Create three instances of the Book class with different book details.
    - Assign these instances to variables: book1, book2, and book3.
4. Print Book Details and Length Status:
    - Use the display_details method to print the details of each book.
    - Use the is_long_book method to print whether each book is long or not.
5. Upload to GitHub:
    - Save your program in a .py file.
    - Upload this file to your ADD 160 directory on GitHub.
    - Copy the link to your file on GitHub.
6. Submit the Link:
    - Submit the GitHub link to your instructor as proof of completion.
    - Sample Output

When you run your program, the output should look like this:

    Title: Python Programming, Author: John Doe, Pages: 150
    Is long book: True

    Title: The Hobbit, Author: J.R.R. Tolkien, Pages: 310
    Is long book: True

    Title: Short Stories, Author: Jane Smith, Pages: 95
    Is long book: False
    
"""

# Create class


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_details(self):
        print(
            f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}\nIs long book: {self.is_long_book()}")

    def is_long_book(self):
        return self.pages > 100


# Create book class instances
book1 = Book(title="Neuromancer", author="William Gibson", pages=336)

book2 = Book(title="Count Zero", author="William Gibson", pages=336)

book3 = Book(title="Mona Lisa Overdrive", author="William Gibson", pages=256)


# main program

def main():
    book1.display_details()
    print()
    book2.display_details()
    print()
    book3.display_details()


main()
