#Variable Length Nonkeyword Argument

def fun(*a,x=12,y=24):
	print("a is",a)
	print("x is",x)
	print("y is",y)

fun(99)
fun("Rasha","Navya",x="Tia",y="Tira")
fun(78,92)	