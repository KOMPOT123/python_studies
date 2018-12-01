class SchoolMember:
    """любой человек"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Cоздан человек: "{0}")'.format(self.name))
    def tell(self):
        '''вывод информации'''
        print('Имя:"{0}"  Возраст: "{1}"'.format(self.name, self.age), end=' ')

class Teacher(SchoolMember):
    """Преподы"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Препод: "{0}")'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    """Cтуденты"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан студент: "{0}")'.format(self.marks))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print("_")#пустая

members = [t, s]
for member in members:
    member.tell()#работает для всех
