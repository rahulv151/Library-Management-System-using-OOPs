class Library:
    def __init__(self):
        self.book_list = []

    def menu(self):
        print("Library Menu:")
        print("1. Create a book")
        print("2. Show books")
        print("3. Issue a book")
        print("4. Return a book")
        print("5. Exit")

    def create_book(self):
        book_name = input("Enter the name of the book: ")
        self.book_list.append(book_name)
        print(f"{book_name} has been added to the library.")

    def show_books(self):
        print("Books in the library:")
        for book in self.book_list:
            print(book)

    def issue_book(self):
        book_issue = input("Enter the name of the book to issue: ")
        if book_issue in self.book_list:
            self.book_list.remove(book_issue)
            print(f"{book_issue} has been issued.")
        else:
            print(f"{book_issue} is not in the library.")

    def return_book(self):
        book_return = input("Enter the name of the book to return: ")
        self.book_list.append(book_return)
        print(f"{book_return} has been returned.")

    def run_library(self):
        while True:
            self.menu()
            choice = input("Enter your choice : ")

            if choice == "1":
                self.create_book()
            elif choice == "2":
                self.show_books()
            elif choice == "3":
                self.issue_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                print("Thanks for visiting !")
                break
            else:
                print("Invalid choice. Please enter a valid choice ")

my_library = Library()
my_library.run_library()
