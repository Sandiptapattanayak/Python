#Hierarchical Inheritance(With parameters)

class Person:
	def __init__(self,n,r):
		self.name=n
		self.roll=r

		def setName(self,n):
			self.name=n
		def getName(self):
			return self.name
			print(self.name,self.roll)

class Student(Person):
	def __init__(self,n,r,m):
		super(). __init__(n,r)
		self.mark=m
	def setMark(self,m):
		self.mark=m
	def getMark(self):
		return self.mark	

class Engstudent(Person):
	def __init__(self,n,r,a):
		super(). __init__(n,r)
		self.age=a
	def setAge(self,a):
		self.age=a
	def getAge(self):

		return self.age
e=Engstudent("Radhya",101,23)
s=Student("Ara",102,80)
print(e.name)
print(s.name)
s.setMark(85)
print(s.getMark())
e.setAge(25)
print(e.getAge())
