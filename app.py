from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model and encoders
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Define expected input features
expected_features = list(label_encoders.keys())
expected_features.remove("y")
expected_features += ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']

def preprocess_input(data):
    df = pd.DataFrame([data])
    for col in label_encoders:
        if col in df.columns and col != "y":
            le = label_encoders[col]
            df[col] = le.transform([df[col].values[0]])
    return df

app = Flask(__name__)

@app.route("/")
def home():
    return "Model microservice is live. Use /predict endpoint."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        missing = [f for f in expected_features if f not in input_data]
        if missing:
            return jsonify({"error": f"Missing features: {missing}"}), 400
        df = preprocess_input(input_data)
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0].max()
        return jsonify({
            "prediction": str(prediction),
            "probability": round(float(probability), 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
