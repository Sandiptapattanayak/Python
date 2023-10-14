#Multilevel inheritance by using constructor(with parameter)

class Person:
	def __init__(self,n,a):
		self.__name=n
		self.__age=a
	def setName(self,n):
		self.__name=n
	def setAge(self,a):
		self.__age=a	
	def getName(self):
		return self.__name
	def getAge(self):
		return self.__age
class Student(Person):
	def __init__(self,n,a,m):
		super(). __init__(n,a)
		self.__mark=m
	def setMark(self,m):
		self.__mark=m
	def getMark(self):
		return self.__mark
class EngStudent(Student):
	def __init__(self,n,a,m,p):
		super(). __init__(n,a,m)
		self.__perecentage=p	
	def setPercentage(self,p):
		self.__percentage=p
	def getPercentage(self):
		return self.__percentage			
ob=EngStudent("Radhya",23,80,70)
ob1=EngStudent("Rayesha",34,90,68)
ob.setName("Rahul")
print("name=",ob.getName())
ob1.setMark(78)
print("mark=",ob.getMark())

