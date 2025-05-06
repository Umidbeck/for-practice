class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrollments = {}

    def enroll(self, course):
        if course.name not in self.enrollments:
            self.enrollments[course.name] = None
            course.add_student(self)

    def set_grade(self, course_name, grade):
        if course_name in self.enrollments:
            self.enrollments[course_name] = grade

    def gpa(self):
        grades = [g for g in self.enrollments.values() if g is not None]
        return sum(grades)/len(grades) if grades else 0
    
class Instructor:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def assign_to(self,course):
        self.courses.append(course)
        course.set_instructor(self)


class Course:
    def __init__(self, name ,max_students=30):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.instructor = None

    def set_instructor(self, insturoctor):
        self.instructor = insturoctor

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)

    def assign_grade(self, student, grade):
        student.set_grade(self.name, grade)


class University:
    def __init__(self):
        self.students = []
        self.courses = []
        self.instructors = []

    def add_student(self, student):
        self.students.append(student) 


    def add_course(self, course):
        self.courses.append(course)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def report(self):
        for student in self.students:
            print(f"{student.name} GPA: {student.gpa(): .2f}")      



# Universitetni yaratamiz
uni = University()

# Kurslar va o‘qituvchilar
python = Course("Python OOP", 2)
ml = Course("Machine Learning")

akmal = Instructor("Akmal")
nargiza = Instructor("Nargiza")

akmal.assign_to(python)
nargiza.assign_to(ml)

# Talabalar
ali = Student("Ali", 1)
vali = Student("Vali", 2)

# Ro‘yxatga olish
ali.enroll(python)
vali.enroll(python)
vali.enroll(ml)

# Baholar qo‘yish
python.assign_grade(ali, 85)
python.assign_grade(vali, 90)
ml.assign_grade(vali, 95)

# Tizimga qo‘shish
uni.add_course(python)
uni.add_course(ml)
uni.add_student(ali)
uni.add_student(vali)
uni.add_instructor(akmal)
uni.add_instructor(nargiza)

uni.report()
 
