#Program using join() method

from threading import *
import time

def fun1():
	for i in range(5):
		time.sleep(3)
		print("Lira")

t1=Thread(target=fun1)
t1.start()
t1.join(5)

for i in range(5):
	print("Riya")	



