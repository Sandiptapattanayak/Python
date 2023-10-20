class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def setName(self,n):
		self.name=n
	def setRoll(self,r):
		self.roll=r
	def setMark(self,m):
		self.mark=m
	def getName(self):
		return self.name
	def getRoll(self):
		return self.roll
	def getMark(self):
		return self.mark
	def update(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m	
	def show(self):
		print("name is=",self.name)
		print("Roll is=",self.roll)
		print("Mark is=",self.mark)
s=Student("Radhya",101,80)
s1=Student("Rasha",102,90)
s.show()
s1.show()
s.setName("Rahul")
s1.update("Rahil",103,35)
print("name is=",s.getName())

		
