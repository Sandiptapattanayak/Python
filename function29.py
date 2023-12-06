#Variable Length Nonkeyword Argument

def fun(x,y,*a):
	print("x =",x)
	print("y=",y)
	print("a=",a)
	
fun(140,150,160,170,180)
fun(2.5,3.6,4,6.7,9.2)
fun("Rajiv","Laira","Ara","Lisa","Riya")	