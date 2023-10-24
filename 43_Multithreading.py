import threading
def disp():
	for i in range(5):
		print("Sandipta")
def show():
	for i in range(5):
		print("Lira")
t1=threading.Thread(target=disp)
t2=threading.Thread(target=show)
t1.start()
t2.start()
