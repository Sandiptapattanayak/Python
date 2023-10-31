import threading,time

def disp(name):

	lock.acquire()
	for i in range(5):
		print("hello ",name)
		time.sleep(0.2)

	lock.release()
lock=threading.Lock()

t1=threading.Thread(target=disp,args=("Ahhan",))
t2=threading.Thread(target=disp,args=("Samisha",))

t1.start()
t2.start()


