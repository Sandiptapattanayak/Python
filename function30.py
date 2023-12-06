#Variable Length Nonkeyword Argument

def fun(*a,x):
	print("x is:",x)
	print("a is:",a)

fun(10,20,30,x=40)
fun("Rahil","Rasha","Rayesha",x="Radhya")	
