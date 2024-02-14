class Library:
    def __init__(self):
        self.file_path = "./books.txt"
        self.file = open(self.file_path, "a+")
    def __del__(self):
        if self.file:
            self.file.close()
    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            title, author, year, pages = line.split(',')
            print(f"Title: {title}, Author: {author}, Year: {year}, Pages: {pages}")
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the first release year: ")
        pages = input("Enter the number of pages: ")
        book_info = f"\n{title},{author},{year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully!")
    def remove_book(self):
      title_to_remove = input("Enter the title of the book to remove: ").strip().lower()
      self.file.seek(0)
      book_lines = self.file.readlines()
      updated_books = [line for line in book_lines if title_to_remove not in line.lower()]
      self.file.seek(0)
      self.file.truncate()
      for line in updated_books:
          self.file.write(line)
      print(f"Book '{title_to_remove}' removed successfully!")
#nesne
lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
