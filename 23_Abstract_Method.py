
# Abstract Class 

from abc import ABC, abstractmethod
 
 
class Person(ABC):
 
    def profession(self):
        pass
 
class Student(Person):
 
    def profession(self):
        print("A person can be a Student")
 
class Teacher(Student):
 
    def profession(self):
        print("A student can be a teacher")
 
class Professor(Student):
 
    def profession(self):
        print("A student can b a Professor")
 
class Engineer(Student):
 
    def profession(self):
        print("A student can be a engineer")
 

R = Student()
R.profession()
 
K = Teacher()
K.profession()
 
R = Professor()
R.profession()
 
K = Engineer()
K.profession()
