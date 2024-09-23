class Library:
    def __init__(self, name, books_list):
        self.name = name
        self.books_list = [book.strip() for book in books_list]  # Remove trailing newlines
        self.books_issued = {}

    def display_books(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.books_list:
            print(book)

    def issue_book(self, book, user):
        if book in self.books_list:
            if book not in self.books_issued.keys():
                self.books_issued.update({book: user})
                print("Book has been issued. Database updated.")
            else:
                print(f"Book is already being used by {self.books_issued[book]}")
        else:
            print("Apologies! We don't have this book in our library")

    def add_book(self, book):
        if book not in self.books_list:
            self.books_list.append(book)
            print("Book added successfully")
        else:
            print("Book already exists in the library")

    def return_book(self, book, user):
        if book in self.books_issued.keys() and self.books_issued[book] == user:
            self.books_issued.pop(book)
            print("Book returned successfully")
        else:
            print("The book does not exist in the database or is not issued to this user")


def main():
    while True:
        print("Welcome to the library")
        choice = """
        1. Display Books
        2. Issue Books
        3. Add Books
        4. Return Books
        """
        print(choice)
        user_input = input("Press q to quit and c to continue: ")
        if user_input.lower() == "c":
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                library.display_books()
            elif user_choice == 2:
                book = input("Enter the name of the book you want to issue: ")
                user = input("Enter your name: ")
                library.issue_book(book, user)
            elif user_choice == 3:
                book = input("Enter the name of the book you want to add: ")
                library.add_book(book)
            elif user_choice == 4:
                book = input("Enter the name of the book you want to return: ")
                user = input("Enter your name: ")
                library.return_book(book, user)
            else:
                print("Invalid choice")
        elif user_input.lower() == "q":
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    database_name = input("Enter the name of the library: ")
    with open(database_name, "r") as book_database:
        book_list = [book.strip() for book in book_database.readlines()]
    library = Library(database_name, book_list)
    main()
