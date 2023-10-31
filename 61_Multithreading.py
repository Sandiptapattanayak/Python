import threading

# Define a shared resource (a variable in this case)
shared_resource = 0

# Create a lock to protect the shared resource
lock = threading.Lock()

# Function that will be executed by multiple threads
def increment_shared_resource():
    global shared_resource
    for _ in range(100000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        shared_resource += 1
        # Release the lock when done
        lock.release()

# Create two threads
thread1 = threading.Thread(target=increment_shared_resource)
thread2 = threading.Thread(target=increment_shared_resource)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Print the final value of the shared resource
print("Shared resource value:", shared_resource)
