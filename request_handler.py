# request_handler.py

import time
from client import simulate_client
from server import Server
from load_balancer import LoadBalancer
from config import NUM_SERVERS

# Global list to reuse servers
servers = [Server(port=9000 + i) for i in range(NUM_SERVERS)]
balancer = LoadBalancer(servers, strategy='round_robin')

def simulate_traffic(count=30):
    for i in range(count):
        simulate_client(f"DashboardRequest {i+1}", balancer)
        time.sleep(0.2)
