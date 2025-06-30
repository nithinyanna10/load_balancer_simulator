import json
import threading
import os

STATE_FILE = "server_state.json"
LOCK = threading.Lock()

def update_state(port, active_connections):
    with LOCK:
        state = {}
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                try:
                    state = json.load(f)
                except:
                    state = {}

        state[str(port)] = active_connections

        # ✅ Add the print statement HERE
        print(f"🔄 update_state() called: port={port}, active_connections={active_connections}")
        print(f"📦 Updated state: {state}")

        with open(STATE_FILE, "w") as f:
            json.dump(state, f)


def get_snapshot():
    with LOCK:
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                try:
                    return json.load(f)
                except:
                    return {}
        return {}
