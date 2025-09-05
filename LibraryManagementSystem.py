# Question
# The Digital Librarian: A Book Management System
# Students will build a command-line application to manage a personal book collection. This project requires defining a Book class (with attributes like title, author, ISBN, genre, and status) and a Library class to manage a collection of Book objects. Students will implement methods for adding new books, searching for books by title or author, sorting the collection by various criteria, and marking books as "read" or "unread." The effective use of lists and dictionaries to store and retrieve book data, alongside adhering to OOP principles, is crucial. Git will be used for version control throughout the development process and for final submission.

# Library Management system

#Books
class Book:
    def __init__(self, title, author, ISBN, genre, read):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.read = read # Boolean variable. True means read Flase means not read
#Library
class Library:
    def __init__(self):
        self.books = []
    
    def get_number_of_books(self):
        return len(self.books)

    def search_book_by_title(self, title):
        books = []
        if self.get_number_of_books() == 0:
            return False
        for book in self.books:
            if title.lower() in book.title.lower():
                books.append(book)
        return books if books else False
    
    def search_book_by_author(self, author):
        books = []
        if self.get_number_of_books() == 0:
            return False
        for book in self.books:
            if author.lower() in book.author.lower():
                books.append(book)
        return books if books else False

    def search_book_by_genre(self, genre):
        books = []
        if self.get_number_of_books() == 0:
            return False
        for book in self.books:
            if genre.lower() in book.genre.lower():
                books.append(book)
        return books if books else False
    
    def search_book_by_ISBN(self, ISBN):
        if self.get_number_of_books() == 0:
            return False
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return False

    def print_mini_report(self):
        print("-"*25)
        print("Mini Report")
        print("-"*25)
        print(f"Total number of books: {self.get_number_of_books()}")
        total_books = self.get_number_of_books()
        if total_books == 0:
            print("Total read books: 0")
            print("Total unread books: 0")
            return
        read_books = self.get_all_read_books()
        unread_books = self.get_all_unread_books()
        if read_books:
            print(f"Total read books: {len(read_books)}")
        else:
            print("Total read books: 0")
        if unread_books:
            print(f"Total unread books: {len(unread_books)}")
        else:
            print("Total unread books: 0")
        percent_read = (len(read_books) / total_books) * 100
        print(f"Percentage of books read: {int(percent_read)}%")
        books_by_genre = self.count_books_by_genre()
        if books_by_genre:
            print("Books by genre:")
            for genre, count in books_by_genre.items():
                print(f"{genre}: {count}")
        else:
            print("No books found by genre.")


    def add_book(self, title, author, ISBN, genre, read):
        if self.search_book_by_title(title):
            return False
        else:
            self.books.append(Book(title, author, ISBN, genre, read))
            return True
    
    def delete_book(self, title):
        if self.search_book_by_title(title):
            for book in self.books:
                if book.title.replace(" ", "").lower() == title.replace(" ", "").lower():
                    self.books.remove(book)
                    return book.title
        else:
            return False
            
    def get_all_books(self):
        if self.get_number_of_books() == 0:
            return False
        return self.books
    
    def get_all_unread_books(self):
        if self.get_number_of_books() == 0:
            return False
        unread_books = []
        for book in self.books:
            if book.read == False:
                unread_books.append(book)
        if len(unread_books) == 0:
            return False
        return unread_books
        
    def get_all_read_books(self):
        if self.get_number_of_books() == 0:
            return False
        read_books = []
        for book in self.books:
            if book.read == True:
                read_books.append(book)
        if len(read_books) == 0:
            return False
        return read_books
    
    def change_book_status(self, title):
        if self.get_number_of_books() == 0:
            return False
        for book in self.books:
            if book.title.replace(" ", "").lower() == title.replace(" ", "").lower():
                if book.read == True:
                    book.read = False
                    return True
                else:
                    book.read = True
                    return True
        return False
        
    def count_books_by_genre(self):
        if self.get_number_of_books() == 0:
            return False
        genre_dictionary = dict()
        
        for book in self.books:
            genre = book.genre
            if genre in genre_dictionary:
                genre_dictionary[genre] += 1
            else:
                genre_dictionary[genre] = 1
                
        return genre_dictionary
    
if __name__ == "__main__":
    library = Library()
    
    # Adding some template books to the library
    if not library.add_book("Project Hail Mary", "Andy Weir", "9780593135204", "Science Fiction", False):
        print("Book is already in the library")
    if not library.add_book("Where the Crawdads Sing", "Delia Owens", "9780735219090", "Literary Fiction", True):
        print("Book is already in the library")
    if not library.add_book("A Court of Thorns and Roses Sarah", "J. Maas", "9781635575569", "Fantasy", True):
        print("Book is already in the library")
    if not library.add_book("The Midnight Library", "Matt Haig", "9780525559474", "Fantasy", True):
        print("Book is already in the library")
    if not library.add_book("Atomic Habits", "James Clear", "9780735211292", "Nonfiction", False):
        print("Book is already in the library")
    if not library.add_book("The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "9781501161933", "Historical Fiction", False):
        print("Book is already in the library")
    if not library.add_book("I'm Glad My Mom Died", "	Min Jin Lee", "9781982185824", "Memoir", False):
        print("Book is already in the library")
    if not library.add_book("Pachinko", "Jennette McCurdy", "9781455563920", "Historical Fiction", False):
        print("Book is already in the library")
    if not library.add_book("Dune", "Frank Herbert", "9780441172719", "Science", False):
        print("Book is already in the library")
    if not library.add_book("The Silent Patient", "Alex Michaelides", "9781250301697", "Thriller", False):
        print("Book is already in the library")
    if not library.add_book("Educated", "Tara Westover", "9780399590504", "Memoir", False):
        print("Book is already in the library")
    if not library.add_book("The Hobbit", "J.R.R. Tolkien", "9780547928227", "Fantasy", True):
        print("Book is already in the library")
    if not library.add_book("The Vanishing Half", "Brit Bennett", "9780525536291", "Literary Fiction", False):
        print("Book is already in the library")
    if not library.add_book("The Night Circus", "Erin Morgenstern", "9780307744432", "Fantasy", False):
        print("Book is already in the library")
    if not library.add_book("Klara and the Sun", "Kazuo Ishiguro", "9780593318171", "Literary Science Fiction", False):
        print("Book is already in the library")
    if not library.add_book("The Song of Achilles", "Madeline Miller", "9780062060624", "Historical Fiction", False):
        print("Book is already in the library")
    if not library.add_book("The Invisible Life of Addie LaRue", "V.E. Schwab", "9780765387561", "Fantasy", True):
        print("Book is already in the library")
    if not library.add_book("All the Light We Cannot See", "Anthony Doerr", "9781501173219", "Historical Fiction", True):
        print("Book is already in the library")
    if not library.add_book("Circe", "Madeline Miller", "9780316556347", "Historical Fiction", True):
        print("Book is already in the library")

    while True:
        print("-"*25)
        print("-"*25)
        print("Library Management System")
        print("-"*25)
        print("-"*25)
        
        print("1. See number of books in library")
        print("2. Search book by Title")
        print("3. Search book by Author")
        print("4. Search book by Genre")
        print("5. Search book by ISBN")
        print("6. Add book")
        print("7. Delete book")
        print("8. See all books in the library")
        print("9. See all unread books in the library")
        print("10. See all read books in the library")
        print("11. Change book status")
        print("12. Count books by genre")
        print("13. Print Mini report")
        print("14. Exit")
        
        try:
            input_number = int(input("Enter Here: "))
        except ValueError:
            print("Invalid input enter again")
            continue
        if input_number == 1:
            print("Total number of books are: ", library.get_number_of_books())
        elif input_number == 2:
            book_name = input("Enter book name: ")
            if book_name.isdigit():
                print("Invalid book name")
                continue
            books = library.search_book_by_title(book_name)
            if books == False:
                print("Book not found in the library")
                continue
            print(f"Total books {len(books)}")
            for book in books:
                print("-"*25)
                print(f"Book Name: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.ISBN}\nBook Genre: {book.genre}\nBook read: {book.read}")
        elif input_number == 3:
            author_name = input("Enter author name: ")
            if author_name.isdigit():
                print("Invalid author name")
                continue
            books = library.search_book_by_author(author_name)
            if books == False:
                print("Author not found in the library")
                continue
            print(f"Total books {len(books)}")
            for book in books:
                print("-"*25)
                print(f"Book Name: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.ISBN}\nBook Genre: {book.genre}\nBook read: {book.read}")
        elif input_number == 4:
            genre_name = input("Enter genre: ")
            if genre_name.isdigit():
                print("Invalid genre name")
                continue
            books = library.search_book_by_genre(genre_name)
            if books == False:
                print("Genre not found in the library")
                continue
            print(f"Total books {len(books)}")
            for book in books:
                print("-"*25)
                print(f"Book Name: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.ISBN}\nBook Genre: {book.genre}\nBook read: {book.read}")
        elif input_number == 5:
            ISBN_number = input("Enter book ISBN: ")
            if ISBN_number.isdigit() == False:
                print("Invalid ISBN number")
                continue
            book = library.search_book_by_ISBN(ISBN_number)
            if book == False:
                print("Book not found in the library")
                continue
            print("-"*25)
            print(f"Book Name: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.ISBN}\nBook Genre: {book.genre}\nBook read: {book.read}")
        elif input_number == 6:
            book_title = input("Enter book title: ")
            book_author = input("Enter book author: ")
            book_ISBN = input("Enter book ISBN: ")
            book_genre = input("Enter genre: ")
            if book_title.isdigit() or book_author.isdigit() or book_genre.isdigit():
                print("Invalid input")
                continue
            if not library.add_book(book_title, book_author, book_ISBN, book_genre, False):
                print("Book is already in the library")
            else:
                print(f"{book_title} added successfully")
        elif input_number == 7:
            book_name = input("Enter book name to be deleted: ")
            if book_name.isdigit():
                print("Invalid book name")
                continue
            book = library.delete_book(book_name)
            if book:
                print(f"{book} deleted")
            else:
                print("Book not found in the library")
        elif input_number == 8:
            books = library.get_all_books()
            if not books:
                print("Library is empty")
            else:
                print(f"Total books {len(books)}")
                for book in books:
                    print("-"*25)
                    print(f"Book Name: {book.title}\nBook Author: {book.author}\nBook ISBN: {book.ISBN}\nBook Genre: {book.genre}\nBook read: {book.read}")
        elif input_number == 9:
            unread_books = library.get_all_unread_books()
            if not unread_books:
                print("Library is either empty or there are no unread books")
            else:
                print(f"Total unread books {len(unread_books)}")
                for book in unread_books:
                    print(f"Book Name: {book.title}")
        elif input_number == 10:
            read_books = library.get_all_read_books()
            if not read_books:
                print("Library is either empty or there are no read books")
            else:
                print(f"Total read books {len(read_books)}")
                for book in read_books:
                    print(f"Book Name: {book.title}")
        elif input_number == 11:
            book_name = input("Enter book name: ")
            if book_name.isdigit():
                print("Invalid book name")
                continue
            book = library.change_book_status(book_name)
            if book:
                print("Book status change")
            else:
                print("Book not found")
        elif input_number == 12:
            genre_dictionary = library.count_books_by_genre()
            if genre_dictionary:
                for genre, count in genre_dictionary.items():
                    print(f"{count} books on {genre}")
            else:
                print("Library is empty")
        elif input_number == 13:
            library.print_mini_report()
        elif input_number == 14:
            break
        else:
            print("-"*25)
            print("-"*25)
            print("Wrong input try again")
            print("-"*25)
            print("-"*25)
 