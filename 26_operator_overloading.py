# Time addition using operator overloading

class Time:											
	def __init__(self,hr,min,sec):
		self.hr=hr
		self.min=min
		self.sec=sec

	def show(self):
		print(self.hr,self.min,self.sec)

	def __add__(self,other):
			T3.hr=self.hr+other.hr
			T3.min=self.min+other.min
			T3.sec=self.sec+other.sec

			if T3.min>=60:
				T3.hr+=1
				T3.min-=60

			if T3.sec>=60:
				T3.min+=1
				T3.sec-=60	
		
			return Time(T3.hr,T3.min,T3.sec)
	def __str__(self):
		return f"{self.hr:02d}:{self.min:02d}:{self.sec:02d}"		


T1=Time(2,35,40)
T2=Time(3,35,25)
T3=Time(0,0,0)
T3=T1+T2	
print("time1:",T1)
print("time2:",T2)
print("time:",T3)	
						
