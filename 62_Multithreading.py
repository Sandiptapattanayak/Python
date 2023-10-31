import threading

# Define a shared resource (a variable in this case)
shared_resource = 0

# Create a reentrant lock to protect the shared resource
lock = threading.RLock()

# Function that will be executed by multiple threads
def increment_shared_resource():
    global shared_resource
    for _ in range(200000):
        # Acquire the reentrant lock before accessing the shared resource
        lock.acquire()
        shared_resource += 1
        # Call another function that also uses the same lock
        increment_shared_resource_nested()
        # Release the reentrant lock when done
        lock.release()

# Function that can be called within the main function
def increment_shared_resource_nested():
    global shared_resource
    # Acquire the reentrant lock again within the same thread
    lock.acquire()
    shared_resource += 1
    # Release the reentrant lock
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
