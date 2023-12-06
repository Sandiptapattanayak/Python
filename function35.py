#Global Variable

a=23
def fun1():
	global a
	a=999
	print(a)

def fun2():
	print(a)

fun1()
fun2()	