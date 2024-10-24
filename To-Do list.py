class Task:
    def __init__(self, description):
        self.description = description
        self.completed  = False
        
    def mark_complete(self):
        self.completed = True
        
    def __str__(self):
        status = "Tugallandi" if self.completed else "Kutmoqda"
        return f"{self.description} - {status}"
    
    
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task_description):
        new_task = Task(task_description)
        self.tasks.append(new_task)
        
    def list_tasks(self):
        if not self.tasks:
            print("Ro'yhatda hechqanday vazifa yo'q")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index+1} . {task}")
                
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index-1].mark_complete()
        else:
            print("Vazifa topilmadi")
            
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index-1)
        else:
            print("Vazifa topilmadi")
            
def menu():
    todo = ToDoList()
    
    while True:
        print("\n1. Vazifa qo'shish")
        print("2. Vazifalarni ro'yxatini ko'rish")
        print("3. Vazifani tugallangan deb belgilash")
        print("4. Vazifani olib tashlash")
        print("5. Chiqish")
        choice = input("Variantni tanlang")
        
        if choice == '1':
            task_discreption = input("Vazifani tafsifini kiriting")
            todo.add_task(task_discreption)
        elif choice == '2':
            todo.list_tasks()
        elif choice == '3':
            todo.list_tasks()
            task_index = int(input("Tugallangan diyish uchun vazifa raqamini kiriting..."))
            todo.mark_task_completed(task_index)
        elif choice == '4':
            todo.list_tasks()
            task_index = int(input("Olib tashlash uchun vazifa raqamini kiriting..."))
            todo.remove_task(task_index)
        elif choice == '5':
            break
        else:
            print("Noto'g'ri variant qaytadan urinib ko'ring")
            
menu()
        