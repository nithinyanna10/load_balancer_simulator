import streamlit as st
import time
from shared_state import get_snapshot
import pandas as pd
from request_handler import simulate_traffic

st.set_page_config(page_title="🛡️ Load Balancer Monitor", layout="wide")

st.title("🛡️ Load Balancer Live Monitor")
load_history = []

placeholder = st.empty()
chart_placeholder = st.empty()

# Trigger traffic from dashboard
if st.button("🚀 Simulate 30 Requests"):
    st.success("Simulating traffic...")
    simulate_traffic()

while True:
    snapshot = get_snapshot()
    timestamp = time.strftime("%H:%M:%S")

    if snapshot:
        ports = list(snapshot.keys())
        loads = list(snapshot.values())
        load_history.append((timestamp, *loads))

        # Display bar chart
        with placeholder.container():
            st.subheader("📊 Current Load")
            for p, l in zip(ports, loads):
                if l > 5:
                    emoji = "🔴"
                elif l >= 3:
                    emoji = "🟡"
                else:
                    emoji = "🟢"
                st.write(f"Server {p}: {l} connections {emoji}")

        # Display line chart over time
        df = pd.DataFrame(load_history, columns=["Time"] + ports)
        df.set_index("Time", inplace=True)
        with chart_placeholder:
            st.line_chart(df)
    else:
        st.info("Waiting for traffic...")

    time.sleep(1)
