import threading
from collections import deque

class LoadBalancer:
    def __init__(self, servers, strategy='round_robin'):
        self.servers = servers
        self.strategy = strategy
        self.lock = threading.Lock()
        self.index = 0  # for round-robin

    def get_server(self):
        with self.lock:
            if self.strategy == 'round_robin':
                server = self.servers[self.index]
                self.index = (self.index + 1) % len(self.servers)
                return server
            elif self.strategy == 'least_connection':
                return min(self.servers, key=lambda s: s.active_connections)
