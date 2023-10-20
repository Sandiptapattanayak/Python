class Person:
	def __init__(self,n,r):
		self.__name=n
		self.__rollno=r
	def  setName(self,n):
		self.__name=n
	def setRollno(self,r):
		self.__rollno=r
	def getName(self):
		return self.__name
	def getRollno(self):
		return self.__rollno

p=Person("muna",1)
p.setName("muna das")
p.setRollno(2);
print("name=",p.getName())
print("rollno=",p.getRollno())

