import time
from config import NUM_SERVERS
from server import Server
from load_balancer import LoadBalancer
from client import simulate_client

if __name__ == "__main__":
    servers = [Server(port=9000 + i) for i in range(NUM_SERVERS)]
    balancer = LoadBalancer(servers, strategy='least_connection')  # or 'round_robin'

    # Simulate 10 client requests
    for i in range(50):
        simulate_client(f"Request {i+1}", balancer)
        print(f"📤 Sent Request {i+1}")
        time.sleep(5)  # slow down so dashboard can catch up

