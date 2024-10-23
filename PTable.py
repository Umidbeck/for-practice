from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ['Ism', 'Yosh', 'Shahar']
table.add_row(['Ali', '23', 'Toshkent'])
table.add_row(['Vali', '44', 'Qarshi'])
print(table)



class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        
car = Car('red', '100mph')
car.speed

class Mylist:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, index):
        return self.data[index]
    
my_list = Mylist([1,2,3,4,5,7,9])
print(my_list[2])