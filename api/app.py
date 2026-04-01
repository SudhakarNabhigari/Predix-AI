from fastapi import FastAPI
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI()

# Load trained model
model = joblib.load("model/model.pkl")


# Home route
@app.get("/")
def home():
    return {"message": "PredictX AI Running"}


# Prediction route with anomaly detection
@app.post("/predict")
def predict(cpu: int, memory: int, latency: int, errors: int):
    
    # Convert input into array
    data = np.array([[cpu, memory, latency, errors]])

    # Model prediction
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1] * 100

    # Risk classification
    if probability > 80:
        risk = "HIGH"
    elif probability > 50:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    # Dynamic cost calculation
    cost = int(probability * 1000)

    # 🔥 Anomaly Detection Logic
    anomalies = []

    if cpu > 85:
        anomalies.append("CPU Spike")
    if memory > 85:
        anomalies.append("Memory Overload")
    if latency > 70:
        anomalies.append("High Latency")
    if errors > 7:
        anomalies.append("Too Many Errors")

    # Return response
    return {
        "outage": int(prediction),
        "probability": round(probability, 2),
        "risk": risk,
        "estimated_loss": cost,
        "anomalies": anomalies
    }