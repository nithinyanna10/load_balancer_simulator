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
            
from shared_state import shared_state

class Server:
    def __init__(self, port):
        self.port = port
        self.active_connections = 0
        self.lock = threading.Lock()

    def handle_request(self, data, client_address):
        with self.lock:
            self.active_connections += 1
            shared_state.update(self.port, self.active_connections)

        print(f"[Server {self.port}] Handling request from {client_address}: {data}")
        import time; time.sleep(1)

        with self.lock:
            self.active_connections -= 1
            shared_state.update(self.port, self.active_connections)
        print(f"[Server {self.port}] Finished processing.")
