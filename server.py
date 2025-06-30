import threading
from shared_state import update_state

class Server:
    def __init__(self, port):
        self.port = port
        self.active_connections = 0
        self.lock = threading.Lock()

    def handle_request(self, data, client_address):
        with self.lock:
            self.active_connections += 1
            update_state(self.port, self.active_connections)

        print(f"[Server {self.port}] Handling request from {client_address}: {data}")
        import time; time.sleep(1)

        with self.lock:
            self.active_connections -= 1
            update_state(self.port, self.active_connections)
        print(f"[Server {self.port}] Finished processing.")
