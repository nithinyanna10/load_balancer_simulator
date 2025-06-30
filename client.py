import socket
import threading

def simulate_client(message, balancer):
    server = balancer.get_server()
    threading.Thread(target=server.handle_request, args=(message, "SimClient")).start()
