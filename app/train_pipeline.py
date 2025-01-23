#%%
import pandas as pd
import joblib
import json
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_pipeline(input_file="data.json", model_file="app/model.pkl", encoders_file="app/encoders.pkl"):
    # Load data
    with open(input_file, "r") as file:
        data = json.load(file)
    df = pd.DataFrame(data)

    # Encode categorical features
    encoders = {}
    for col in ["user_agent", "tls_ja3"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    # Train-test split
    X = df.drop("is_anomaly", axis=1)
    y = df["is_anomaly"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Ensure the directory for saving the model exists
    os.makedirs(os.path.dirname(model_file), exist_ok=True)
    os.makedirs(os.path.dirname(encoders_file), exist_ok=True)

    # Save model and encoders
    joblib.dump(model, model_file)
    joblib.dump(encoders, encoders_file)

    from sklearn.metrics import classification_report, accuracy_score

    # Evaluate on the test set
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Accuracy: {acc}")
    print(f"Classification Report:\n{report}")


    print("Model and encoders saved successfully!")

if __name__ == "__main__":
    train_pipeline()
