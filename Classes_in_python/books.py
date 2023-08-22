class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    def display_info(self):
        print("Title :", self.title)
        print("Author", self.author)
        print("ISBN :", self.isbn)
        print("Quantity", self.quantity)

class Book_Inventory:
    def __init__(self):
        self.Book = {}
    def add_book(self, Book):
        self.Book[Book.isbn] = Book
    def update_book_quantity(self, isbn, new_quantity):
        if isbn in self.Book:
            self.Book[isbn].update_quantity(new_quantity)
        else:
            print(f"Book with isbn {isbn}Not found")
    def display_inventory(self):
        print("Book inventory")
        for isbn, book in self.Book.items():
            print("ISBN :", isbn)
            book.display_info()

def main():
    book1 = Book("Book 1", "Author 1", "Isbn12442", 10)
    book2 = Book("Book 2", "Author 2", "Isbn12332", 10)
    book3 = Book("Book 3", "Author 3", "Isbn12222", 10)

    inventory = Book_Inventory()

    inventory.add_book(book1)
    inventory.add_book(book2)
    inventory.add_book(book3)

    inventory.update_book_quantity("Isbn12442", 5)
    inventory.update_book_quantity("Isbn12332", 25)
    inventory.update_book_quantity("Isbn12222", 30)

    inventory.display_inventory()

if __name__ == "__main__":
    main()