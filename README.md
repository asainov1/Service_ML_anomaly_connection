# Service_ML: Anomaly Detection Service

## Description
This project implements a FastAPI-based microservice for anomaly detection using Logistic Regression.

## Features
- `/predict`: Predict if a given connection is anomalous.
- `/train`: Retrain the Logistic Regression model.

## Setup
1. Clone the repository:

2. Navigate to the project directory:

3. Install dependencies:

4. Run the FastAPI application:


## Endpoints
### `/`
- **Method:** `GET`
- **Description:** Health check for the service.

### `/predict`
- **Method:** `POST`
- **Description:** Predict if a connection is anomalous.

### `/train`
- **Method:** `POST`
- **Description:** Retrain the model.

## Example Request
### `/predict`
```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{
 "user_agent": "Mozilla/5.0 (Windows)",
 "tls_ja3": "769,47-53-255,0-23-65281-10-11,29-23",
 "ttl": 128
}'


---

### **6. Add and Commit Your Files**
Add your files to Git and commit them:
```bash
git add .
git commit -m "Initial commit: Completed anomaly detection test"
