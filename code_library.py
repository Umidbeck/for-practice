class Book:
    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} kitobi ijaraga olindi.")
        else:
            print(f"{self.title} kitob hozirda mavjud emas.")

    def return_book(self):
        self.available = True
        print(f"{self.title} kitobi kutubxonaga qaytarildi.")

    def __str__(self):
        status = ",avjud" if self.available else 'mavjud emas'
        return f"{self.title} - {self.author}, {self.year} yilda cho etilgan ({status})"
        

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.borrowed_books = []

    def borrov_book(self, book):
        if len(self.borrowed_books) < 3:
            book.borrow()
            if not book.available:
                self.borrowed_books.append(book)
        else:
            print(f"{self.name}, siz maksimal 3 kitib olishingiz mumkin.")

    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name}, {self.age} yoshda"
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def ad_book(self, book):
        self.books.append(book)
        print(f"{book.title} kitobi kutubxonaga qo'shildi.")

    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} kutubxonaga a'zo bo'ldi")

    def show_books(self):
        for book in self.books:
            print(book)


libary = Library()
book1 = Book("Alisher Navoiy:Xamsa", "Alisher Navoiy", 1501)
book2 = Book("O'zbek tili", "Yozuvchilar uyishmasi", 2020)
book3 = Book('Python', "Anvar Narzullayev", 2021)


libary.ad_book(book1)
libary.ad_book(book2)
libary.ad_book(book3)



user1 = User("Vali", 22)
user2 = User("Ali", 80)


libary.register_user(user1)
libary.register_user(user2)


user1.borrov_book(book1)
user2.borrov_book(book1)

user1.return_book(book1)