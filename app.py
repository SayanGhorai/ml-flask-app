from flask import Flask, request, jsonify
import joblib  # For loading the model
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

# 🆕 Fix: Add a home route to solve 404 error
@app.route('/')
def home():
    return "Welcome to the ML Flask App!"

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)  # Convert input to 2D array
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
