# 🚀 PredictX AI

AI-powered real-time system monitoring and outage prediction dashboard.

---

## 📌 Overview

PredictX AI is an intelligent monitoring system that analyzes system metrics such as CPU usage, memory usage, latency, and error rates to predict potential system outages. It provides real-time insights, risk levels, anomaly detection, and estimated financial impact through an interactive dashboard.

---

## ✨ Features

* 🔍 Real-time system monitoring (Manual & Live modes)
* 🤖 AI-based outage prediction
* 📊 Risk classification (Low / Medium / High)
* 💰 Estimated cost impact
* 🚨 Anomaly detection (CPU spike, memory overload, high latency, errors)
* 📈 Interactive charts and analytics
* ⚡ Auto-updating live dashboard

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Machine Learning:** Scikit-learn
* **Visualization:** Plotly
* **System Metrics:** psutil
* **Deployment:** AWS EC2

---

## 📂 Project Structure

PredictX-AI/

├── api/
│   └── app.py

├── dashboard/
│   └── app.py

├── model/
│   └── model.pkl

├── data/
│   └── history.csv

└── README.md

---

## ⚙️ How to Run Locally

### 1. Clone the repository

git clone https://github.com/your-username/PredictX-AI.git
cd PredictX-AI

---

### 2. Install dependencies

pip install fastapi uvicorn streamlit pandas numpy scikit-learn joblib requests plotly psutil streamlit-autorefresh

---

### 3. Run backend

uvicorn api.app:app --reload

---

### 4. Run frontend

streamlit run dashboard/app.py

---

### 5. Open in browser

http://localhost:8501

---

## 🌐 Deployment

This project can be deployed on AWS EC2 by running both FastAPI and Streamlit servers and exposing ports 8000 and 8501.

---

## 💡 Use Cases

* System health monitoring
* Early outage detection
* IT infrastructure analysis
* DevOps dashboards

---

## 📸 Screenshots

(Add your dashboard screenshots here)

---

## 💬 Author

Your Name

---

## 🚀 Future Enhancements

* Email/SMS alert system
* Advanced anomaly detection
* Real-time streaming data
* Custom domain deployment
