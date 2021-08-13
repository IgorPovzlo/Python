

class Student():
    def __init__(self, name, surname ):
        self.name = name
        self.surname = surname
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(int(grade))

    def get_grades(self):
        return self.grades

    def get_info(self):
        return [self.name + ' ' + self.surname] +self.grades

    def get_name(self):
        return self.name + ' ' + self.surname

x = Student("Иван", "Иванов")
x.add_grade(10)
x.add_grade(8)
x.add_grade(10)
x.add_grade(10)
x.add_grade(2)


y = Student("Евгений","Никифоров")
y.add_grade(5)
y.add_grade(8)
y.add_grade(1)
y.add_grade(7)
y.add_grade(2)


z = Student("Василий","Кошкин")
z.add_grade(1)
z.add_grade(6)
z.add_grade(4)
z.add_grade(2)
z.add_grade(3)



class Group():
    def __init__(self, group_name):
        self.group_name = group_name
        self.lst = []

    def add_group(self, student):
            self.lst.append(student)


    def get_ifo_student(self):
        print ('Группа студентов:', self.group_name)
        for student in self.lst:
            print(student.get_info())
    def get_name_student(self):
        print ('Группа студентов:', self.group_name)
        for student in self.lst:
            print(student.get_name())


gr = Group("Python")
gr.get_name_student()
print()
gr.add_group(x)
gr.get_name_student()
print()
gr.add_group(y)
gr.add_group(z)
gr.get_ifo_student()
