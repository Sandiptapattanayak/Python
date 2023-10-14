#Multilevel inheritance by using function(without parameter) 

class Person:
	def type(self):
		print("Every person has some profession")

class Costumer(Person):
	def type(self):
		super(). type()
		print("A person can be a costumer")

class Student(Costumer):
	def type(self):
		super(). type()
		print("A costumer can be a student")

ob=Student()
ob.type()
