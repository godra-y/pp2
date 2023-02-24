#Human
#gender = m/f
#printInfo()
class Human:
    def printTr(n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j,end='')
            print()
    printTr(4)
    def __init__(self, gender):
        self.gender=gender
    def printInfo(self):
        print(self.gender)
p=Human("female")
print(p.gender)
class Person(Human):
    def __init__(self, name, nationality, gender):
        super().__init__(gender)
        self.name=name
        self.nationality=nationality
    def printInfo(self):
        print(self.name, self.nationality, self.gender)
    def setSurname(self, surname):
        self.surname=surname
    def getSurname(self):
        print(self.surname)
class Student(Person):
    def __init__(self, name, nationality, id, gender):
        super().__init__(name, nationality, gender)
        self.id=id
    def printInfo(self):
        print(self.name, self.nationality, self.id, self.gender)
class Teacher(Person):
    def __init__(self, name, nationality, tid, gender):
        super().__init__(name, nationality, gender)
        self.tid=tid
    def printtInfo(self):
        print(self.name, self.nationality, self.tid, self.gender)

p1=Student("Alnura", "kazakh", "22b030399", "female")
p1.printInfo()
p2=Teacher("Arnur", "kazakh", "22b030399", "male")
p2.printtInfo()
