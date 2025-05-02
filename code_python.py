class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def depost(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm qo'shildi. Yangi balans: {self.__balance} so'm")
        else:
            print("Noto'g'ri miqdor!!!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} so'm yichildi. Balansingizda: {self.__balance} so'm qoldi.")
        else:
            print("Yitarli mablag' ,abjud emas.")

    def get_balance(self):
        return self.__balance
    
#account1 = BankAccount('Ali', 1000)
#account1.depost(500)
#account1.withdraw(700)
#print("Sizning balansingizda", account1.get_balance())

#--------------------------------------------------------------------------------------------------------

class Customer:
    def __init__(self, name):
        self.name = name

    def get_discount(self):
        return 5
    
class VIPCustomer(Customer):
    def get_discount(self):
        return 20
    

    
client1 = Customer('Vali')
client2 = VIPCustomer("Zarin")



print(f"{client1.name} uchun chegirma: {client1.get_discount()}%")
print(f"{client2.name} uchun chegirma: {client2.get_discount()}% ")