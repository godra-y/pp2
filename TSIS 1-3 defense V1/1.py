class Person:
    def __init__(self, name, nationality):
        self.name=name
        self.nationality=nationality
    def printInfo(self):
        print(self.name, self.nationality)
    def setSurname(self, surname):
        self.surname=surname
    def getSurname(self):
        print(self.surname)
class Student(Person):
    def __init__(self, name, nationality, id):
        super().__init__(name, nationality)
        self.id=id
    def printInfo(self):
        print(self.name, self.nationality, self.id)
class Teacher(Person):
    def __init__(self, name, nationality, tid):
        super().__init__(name, nationality)
        self.tid=tid
    def printtInfo(self):
        print(self.name, self.nationality, self.tid)
p1=Student(input(), input(), input())
p1.printInfo()
p2=Teacher(input(), input(), input())
p2.printtInfo()
