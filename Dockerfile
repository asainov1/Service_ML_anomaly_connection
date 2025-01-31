FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn joblib

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
