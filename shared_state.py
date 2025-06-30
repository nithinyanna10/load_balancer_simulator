import threading

class SharedState:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

    def update(self, server_port, active_connections):
        with self.lock:
            self.data[server_port] = active_connections

    def get_snapshot(self):
        with self.lock:
            return dict(self.data)

shared_state = SharedState()
