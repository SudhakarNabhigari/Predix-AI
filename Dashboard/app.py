import streamlit as st
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import psutil
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="PredictX AI", layout="wide")

# 🔥 PREMIUM DARK UI
st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 PredictX AI - Smart Monitoring Dashboard")

# 🔁 Auto refresh
st_autorefresh(interval=2000, key="refresh")

# Sidebar
mode = st.sidebar.radio("Select Mode", ["Manual", "Live System"])

# Input Mode
if mode == "Manual":
    cpu = st.sidebar.slider("CPU (%)", 0, 100, 50)
    memory = st.sidebar.slider("Memory (%)", 0, 100, 50)
    latency = st.sidebar.slider("Latency", 0, 100, 20)
    errors = st.sidebar.slider("Errors", 0, 20, 2)

else:
    real_cpu = psutil.cpu_percent()
    real_memory = psutil.virtual_memory().percent

    cpu = int(real_cpu + np.random.randint(-5, 6))
    memory = int(real_memory + np.random.randint(-5, 6))
    latency = int(np.random.randint(10, 80))
    errors = int(np.random.randint(0, 10))

    cpu = max(0, min(cpu, 100))
    memory = max(0, min(memory, 100))

    st.sidebar.info("⚡ Live fluctuating system data")

# Top Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("CPU", f"{cpu}%")
col2.metric("Memory", f"{memory}%")
col3.metric("Latency", f"{latency} ms")
col4.metric("Errors", errors)

st.write("---")

# API Call
try:
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "cpu": int(cpu),
            "memory": int(memory),
            "latency": int(latency),
            "errors": int(errors)
        },
        timeout=5
    )

    result = response.json()

    prob = result.get("probability", 0)
    risk = result.get("risk", "UNKNOWN")
    cost = result.get("estimated_loss", 0)
    anomalies = result.get("anomalies", [])

except:
    st.error("🚨 Backend not running")
    prob, risk, cost, anomalies = 0, "ERROR", 0, []

# Display Prediction
colA, colB = st.columns(2)

with colA:
    if risk == "HIGH":
        st.error(f"🚨 HIGH RISK ({prob}%)")
    elif risk == "MEDIUM":
        st.warning(f"⚠️ MEDIUM RISK ({prob}%)")
    elif risk == "LOW":
        st.success(f"✅ LOW RISK ({prob}%)")
    else:
        st.warning("⚠️ No valid prediction")

with colB:
    st.metric("💰 Estimated Loss", f"₹ {cost}")

# 🔥 ANOMALY ALERTS
st.subheader("🚨 Anomaly Detection")

if len(anomalies) > 0:
    for anomaly in anomalies:
        st.error(f"⚠️ {anomaly}")
else:
    st.success("✅ No anomalies detected")

st.write("---")

# Gauge Chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=prob,
    title={'text': "Outage Risk %"},
    gauge={'axis': {'range': [0, 100]}}
))
st.plotly_chart(fig, use_container_width=True)

st.write("---")

# Charts
df = pd.DataFrame({
    "Metric": ["CPU", "Memory", "Latency", "Errors"],
    "Value": [cpu, memory, latency, errors]
})

col1, col2 = st.columns(2)

with col1:
    fig2 = px.pie(df, names="Metric", values="Value", hole=0.5)
    st.plotly_chart(fig2, use_container_width=True)

with col2:
    st.bar_chart(df.set_index("Metric"))

st.write("---")

# Trend
st.subheader("📈 Live Trend")

trend = pd.DataFrame({
    "CPU": np.random.randint(cpu-10, cpu+10, 10),
    "Memory": np.random.randint(memory-10, memory+10, 10),
    "Latency": np.random.randint(10, 80, 10)
})

st.line_chart(trend)

st.write("---")

# History
st.subheader("📜 Prediction History")

try:
    history = pd.read_csv("data/history.csv")
    st.dataframe(history.tail(5))
except:
    st.write("No history available")

st.write("---")
st.markdown("<center>🔥 PredictX AI - Production Dashboard</center>", unsafe_allow_html=True)