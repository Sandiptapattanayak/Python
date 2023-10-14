#Single inheritance by using method(with parameter)

class Vehicle:							
	def show(self,brand,colour):
		self.brand=brand
		self.colour=colour
		print("A",self.colour,self.brand,"vehicle")

class Car(Vehicle):
	def show(self,colour,brand,model):
		super().show(brand,colour)
		self.model=model
		print("A",self.colour,self.brand,self.model,"car")
		
obj1=Car()
obj1.show("White","TATA","Nexon")
