
# 🛡️ Load Balancer Simulator

A multithreaded load balancer simulator built in Python that distributes client requests to backend servers using Round-Robin or Least-Connection strategies. It includes a real-time dashboard powered by Streamlit to visualize server load, traffic simulation, and live performance.

---

## 🚀 Features

- ✅ Round-Robin and Least-Connection load balancing algorithms
- ✅ Multithreaded server simulation using Python threads
- ✅ Live dashboard using Streamlit
- ✅ Real-time server load chart over time 📈
- ✅ Emoji indicators for server load (🟢🟡🔴)
- ✅ Button to simulate traffic directly from the dashboard

---

## 📁 Folder Structure

```
load_balancer_simulator/
├── main.py                  # Main script to simulate traffic
├── client.py                # Simulated clients
├── config.py                # Server configuration
├── server.py                # Server class with active connection handling
├── load_balancer.py         # Load balancing logic
├── shared_state.py          # File-based shared state management
├── dashboard.py             # Streamlit dashboard with chart + emoji indicators
├── request_handler.py       # Dashboard-triggered traffic simulation
├── server_state.json        # Live server state store
└── requirements.txt
```

---

## ⚙️ How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run Load Simulation
```bash
python main.py
```

### 3. Run the Dashboard
```bash
streamlit run dashboard.py
```

> You can also use the 🚀 button on the dashboard to simulate new traffic.

---

## 🧠 Tech Stack

- Python (Threading, Sockets)
- Streamlit (Real-time UI)
- Pandas (Chart history)
- JSON-based state sharing

---

## 📊 Dashboard Preview

- Bar chart showing live active connections per server
- Line chart for load over time
- Emoji-based indicators:
  - 🟢 = Low load
  - 🟡 = Moderate
  - 🔴 = High load

---

## 🙌 Future Enhancements

- Auto-scaling servers on demand
- Failure simulation and retries
- Real socket-based communication between services
- Export load chart to PNG or PDF

---

## 🧪 Author

Made by Nithin Reddy Yanna 🚀

