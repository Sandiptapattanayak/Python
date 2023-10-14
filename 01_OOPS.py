class Car:
	def __init__(self,brand,model):
		self.brand=brand
		self.model=model
	def show(self):
		print(self.brand,self.model)
	def move(self):
		print("Drive!")
class Bike:
	def __init__(self,brand,model):
		self.brand=brand
		self.model=model
	def show(self):
		print(self.brand,self.model)
	def move(self):
		print("Ride!")
class Truck:
	def __init__(self,brand,model):
		self.brand=brand
		self.model=model
	def show(self):
		print(self.brand,self.model)
	def move(self):
		print("Fly")
c=Car("TATA","Nexon")
c.show()
c.move()
b=Bike("Hero","splender")
b.show()
b.move()
t=Truck("TATA",407)
t.show()
t.move()
