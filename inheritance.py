class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

cat = Cat()
#cat.walk()

dog = Dog()
#dog.walk()


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname + " "+ self.lname)

person = Person("Suvendu", "Chakrabarty")
person.print_name()

class Student(Person):
    def __init__(self,fname, lname, year):
        super().__init__(fname,lname)
        self.gradutation_year = year

student = Student("xx", "yy", 2023)
print(student.gradutation_year)

