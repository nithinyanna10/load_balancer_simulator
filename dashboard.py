import streamlit as st
import time
from shared_state import get_snapshot

st.set_page_config(page_title="Load Balancer Monitor", layout="wide")
st.title("🛡️ Load Balancer Live Monitor")
placeholder = st.empty()

while True:
    snapshot = get_snapshot()
    if snapshot:
        ports = list(snapshot.keys())
        loads = list(snapshot.values())

        with placeholder.container():
            st.bar_chart(loads)
            st.write("🔄 Updated live every second")
    else:
        st.info("Waiting for traffic...")

    time.sleep(1)
