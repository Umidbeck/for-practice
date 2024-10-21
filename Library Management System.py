class Book:
    def __init__(self, nomi, muallifi, janri, kitob_raqami, mavjudmi = True ):
        self.nomi = nomi
        self.muallifi = muallifi
        self.janri = janri
        self.kitob_raqami = kitob_raqami
        self.mavjudmi = mavjudmi
        
        
    def display_info(self):
        return f"Bizning kutubxonamizda {self.nomi} kitobi muallif {self.muallifi} janri{self.janri} bizda hozirda {self.mavjudmi}"
    
    def update_info(self, nomi = None, muallifi = None, janri = None, kitob_raqami = None):
        if nomi:
            self.nomi = nomi
        if muallifi:
            self.muallifi = muallifi
        if janri:
            self.janri = janri
        if kitob_raqami:
            self.kitob_raqami = kitob_raqami
            
    def __str__(self):
        return self.nomi
        
            
    
class Reader:
    def __init__(self, ism, oqivchi_raqami, olingan_kitoblar = []):
        self.ism = ism
        self.oquvchi_raqami = oqivchi_raqami
        self.olingan_kitoblar = olingan_kitoblar
            
            
    def display_info(self):
        return f"{self.ism} {self.oquvchi_raqami} bizdan olgan kitoblari {self.olingan_kitoblar}"
        
    def add_book(self, book):
        self.olingan_kitoblar.append(book.nomi)
            
    def remove_book(self, book_1):
        for book in self.olingan_kitoblar:
            if book == book_1:
                self.olingan_kitoblar.remove(book)
            else: 
                return "Bunday kitob yo'q"
            
    def __str__(self):
        return self.olingan_kitoblar
                
        
class LibraryManagementSystem:
    def __init__(self):
        self.oquvchilar_royhati = []
        self.kitoblar_royhati = []
            
    def add_book(self, book):
        self.kitoblar_royhati.append(book)
            
    def remove_book(self, book):
        self.kitoblar_royhati = [book_1 for book_1 in self.kitoblar_royhati if book_1.kitob_raqami != book]
            
    def register_oquvchi(self, oquvchi):
        self.oquvchilar_royhati.append(oquvchi)
            
    def remove_oquvchi(self, oquvchi_name):
        self.oquvchilar_royhati = [oquvchi for oquvchi in self.oquvchilar_royhati if oquvchi != oquvchi_name ]
            
    def lend_book(self, oquvchi_id, kitob_id):
        oquvchi = next((oquvchi for oquvchi in self.oquvchilar_royhati if oquvchi_id == oquvchi.oquvchi_raqami), None)
        kitob  = next((kitob for kitob in self.kitoblar_royhati if kitob.kitob_raqami == kitob_id), None)
            
        if oquvchi and kitob and kitob.mavjudmi:
            oquvchi.add_book(kitob)
            kitob.mavjudmi = False
            print(f"{oquvchi.ism} kitobini oldi {kitob.nomi}")
        else:
            print("Kitob yoki o'quvchi topilmadi")
                
    def return_book(self, oquvchi_id, kitob_id):
        oquvchi = next((oquvchi for oquvchi in self.oquvchilar_royhati if oquvchi_id == oquvchi.oquvchi_raqami), None)
        kitob  = next((kitob for kitob in self.kitoblar_royhati if kitob.kitob_raqami == kitob_id), None)
        if oquvchi and kitob:
            oquvchi.remove_book(kitob)
            print(f"{oquvchi.ism} kitobni qaytardi {kitob.nomi}")
                
        
    def list_books(self):
            for royhat in self.kitoblar_royhati:
                print(royhat.display_info())
                        
    def list_oquvchilar(self):
        for oquvchi in self.oquvchilar_royhati:
            print(oquvchi.display_info())
                
                
                
def main():
    library = LibraryManagementSystem()

    # Kitoblar va o'quvchilar qo'shish
    library.add_book(Book("Python 101", "John Doe", "Dasturlash", 1))
    library.add_book(Book("OOP in Python", "Jane Smith", "Dasturlash", 2))
    library.register_oquvchi(Reader("Ali", 101))
    library.register_oquvchi(Reader("Vali", 102))

    # Kitoblarni ko'rsatish
    print("\nKitoblar ro'yxati:")
    library.list_books()

    # Kitobni ijaraga berish
    print("\nKitobni ijaraga berish:")
    library.lend_book(101, 1)

    # O'quvchini ko'rsatish
    print("\nO'quvchilar ro'yxati:")
    library.list_oquvchilar()

    # Kitobni qaytarish
    print("\nKitobni qaytarish:")
    library.return_book(101, 1)

    # O'zgartirish va ko'rsatish
    print("\nO'zgartirilgan kitoblar ro'yxati:")
    library.list_books()


if __name__ == "__main__":
    main()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
            
            
            
            
            
            
            
            