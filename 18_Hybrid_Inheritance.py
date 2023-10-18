# Hybrid Inheritance
class Vehicle:
    
    def __init__(self):
        print("Has number of wheels")
    
                
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        print("Has two wheels")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print('Has four wheels')

class Roadway_Vehicle(Bike,Car):
    def __init__(self):
        super().__init__()
        print("Uses road for transportation")        

R=Roadway_Vehicle()