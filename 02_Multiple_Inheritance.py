Multiple Inheritance

class Person:
	def __init__(self):
		super(). __init__()
		print("A student comes under Person class")

class Student:
	def __init__(self):
		print("A Engineering student comes under student class ")

class Engstudent(Person,Student):
	def __init__(self):
		super(). __init__()

e=Engstudent()	
