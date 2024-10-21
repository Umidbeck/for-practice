class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        
    def desplay_info(self):
        return f"Xodimning ismi {self.name} yoshi {self.age} lavozimi {self.position} maoshi {self.salary}"
    
    def update_info(self, name = None, age = None, position = None, salary = None):
        if name:
            self.name = name
        if age:
            self.age = age
        if position:
            self.position = position
        if salary:
            self.salary = salary
            
    
class EmployeeManagement_system:
    def __init__(self):
        self.list = []
        
    def add_employees(self, employee):
        self.list.append(employee)
        
    def remove_employee(self, name):
        for emp in self.list:
            if emp.name == name:
                self.list.remove(emp)
                
                return
            
    def list_employees(self):
        if self.list:
            
            for emp in self.list:
                print(emp.desplay_info())
        else:
            print("Ro'yhat bo'sh")


    def update_employees(self, name, **kwargs):
        for emp in self.list:
            if emp == name:
                emp.update_info(**kwargs)
                return
            
                        
                    
        
        
        
        
        