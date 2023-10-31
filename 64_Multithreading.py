import threading
import queue
import time

message_queue = queue.Queue()

def sender_thread():
    messages = ["Hello", "How are you?", "Goodbye"]
    for message in messages:
        message_queue.put(message)
        print(f"Sent: {message}")
        time.sleep(1)

def receiver_thread():
    while True:
        message = message_queue.get()
        print(f"Received: {message}")
        message_queue.task_done()

sender = threading.Thread(target=sender_thread)
receiver = threading.Thread(target=receiver_thread)

sender.start()
receiver.start()

sender.join()

