#%%
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import logging

# Setup FastAPI app
app = FastAPI()

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and encoders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_FILE = os.path.join(BASE_DIR, "model.pkl")
ENCODERS_FILE = os.path.join(BASE_DIR, "encoders.pkl")

try:
    model = joblib.load(MODEL_FILE)
    encoders = joblib.load(ENCODERS_FILE)
    logger.info("Model and encoders loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model or encoders: {e}")
    raise RuntimeError("Failed to load model or encoders.")

# Input schema for /predict endpoint
class ConnectionData(BaseModel):
    user_agent: str
    tls_ja3: str
    ttl: int

@app.on_event("startup")
def startup_event():
    logger.info("FastAPI application started.")

@app.get("/")
def read_root():
    return {"message": "Service is running"}

@app.post("/predict")
def predict(data: ConnectionData):
    try:
        # Prepare data for prediction
        input_data = {
            "user_agent": [data.user_agent],
            "tls_ja3": [data.tls_ja3],
            "ttl": [data.ttl],
        }
        df = pd.DataFrame(input_data)

        # Encode features
        for col in ["user_agent", "tls_ja3"]:
            if df[col].iloc[0] not in encoders[col].classes_:
                raise HTTPException(status_code=400, detail=f"Unknown value for {col}: {df[col].iloc[0]}")
            df[col] = encoders[col].transform(df[col])

        # Predict
        prediction = model.predict(df)[0]
        return {"is_anomaly": int(prediction)}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/train")
def train():
    try:
        from train_pipeline import train_pipeline
        train_pipeline()
        logger.info("Model retrained successfully.")
        return {"message": "Model retrained successfully!"}
    except Exception as e:
        logger.error(f"Error during training: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status")
def get_status():
    return {
        "model": "Logistic Regression",
        "encoders_loaded": True,
        "version": "1.0.0"
    }