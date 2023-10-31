import threading,time 

class MyThread(threading.Thread):

	def __init__(self,name):
		super().__init__()
		self.name=name

	def run(self):
		lock.acquire()
		for i in range(5):
			print("hello ",self.name)
			time.sleep(0.2)

		lock.release()
lock=threading.Lock()

t1=MyThread("Lira")
t2=MyThread("Samisha")

t1.start()
t2.start()
