import socket
import threading

class Server:
    def __init__(self, port):
        self.port = port
        self.active_connections = 0
        self.lock = threading.Lock()

    def handle_request(self, data, client_address):
        with self.lock:
            self.active_connections += 1
        print(f"[Server {self.port}] Handling request from {client_address}: {data}")
        # Simulate processing
        import time; time.sleep(1)
        print(f"[Server {self.port}] Finished processing.")
        with self.lock:
            self.active_connections -= 1
