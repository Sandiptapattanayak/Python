# Program on Multithreading using class 

import threading
class Test:
	def disp(self):
		for i in range(5):
			print("hello")
	def show(self):
		for i in range(5):
			print("bye")
t=Test()
t1=threading.Thread(target=t.disp)
t2=threading.Thread(target=t.show)
t1.start()
t2.start()

