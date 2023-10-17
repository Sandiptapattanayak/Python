#Hierarchical inheritance(without parameter)

class Person:
	def __init__(self):
		print("Person Class")
class Student(Person):
	def __init__(self):
		super(). __init__()
		print("Student Class")	
class Engstudent(Person):
	def __init__(self):
		super(). __init__()
		print("Engstudent Class")
e=Engstudent()
s=Student()
