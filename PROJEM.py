# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 21:12:12 2024

@author: Zeynep
"""

class Library:
    def __init__(self):
        self.filename = "books.txt"
        self.file = open(self.filename, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print(f"Book Name: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        title = input("Enter the title of the book to be removed: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if title not in book:
                updated_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book removed successfully!")

def main():
    lib = Library()
    while True:
        print("\n*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        choice = input("Enter your choice (1-3) or 'q' to quit: ")
        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice.lower() == 'q':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
