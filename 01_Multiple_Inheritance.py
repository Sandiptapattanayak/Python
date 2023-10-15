#Multiple Inheritance(with parameters)

class Person:
	def __init__(self,n,r,m,a):
		self.name=n
		self.roll=r
		self.mark=m
		super(). __init__(a)

	def setName(self,n):
		self.name=n
	def getName(self):
		return self.name
	def setRoll(self,r):
		self.roll=r
	def getRoll(self):
		return self.roll
	def setMark(self,m):
		self.mark=m
	def getMark(self):
		return self.mark

class Student:
	def __init__(self,a):
		self.age=a	
	def setAge(self,a):
		self.age=a
	def getAge(self):
		return self.age

class Engstudent(Person,Student):
	def __init__(self,n,r,m,a):
		super(). __init__(n,r,m,a)
		
e=Engstudent("Radhya",121,80,15)	
print(e.getName())	
e.setName("Rahul")
print(e.getName())
