import threading

lock = threading.Lock()

def do_work():
    with lock:
        print("Work in progress")
        # Additional code here

t1 = threading.Thread(target=do_work)
t2 = threading.Thread(target=do_work)

t1.start()
t2.start()
