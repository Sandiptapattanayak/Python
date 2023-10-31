
import threading

# Create a semaphore with an initial value of 3
semaphore = threading.Semaphore(3)

# Function representing a task that requires access to the shared resource
def perform_task(task_id):
    with semaphore:
        print(f"Task {task_id} is using the shared resource")
        # Simulate some work
        for _ in range(3):
            pass
        print(f"Task {task_id} has finished")

# Create multiple threads to perform tasks
threads = []

for i in range(5):
    thread = threading.Thread(target=perform_task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All tasks have completed.")


