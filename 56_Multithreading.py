#Program using join() method


from threading import *

def fun1():
	for i in range(5):
		print("Lira")

def fun2():
	t1.join()
	for i in range(5):
		print("Ahhan")

def fun3():
	for i in range(5):
		print("Riya")		

t1=Thread(target=fun1)



t2=Thread(target=fun2)		

	

t3=Thread(target=fun3)
t1.start()
t2.start()
t3.start()


