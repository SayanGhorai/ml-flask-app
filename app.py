from flask import Flask, request, jsonify
import joblib  # For loading the model
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    print("Received request:", request.data)  # Debugging line
    print("Content-Type:", request.content_type)  # Debugging line
    
    # Check if request data is JSON
    if request.is_json:
        data = request.get_json()
        print("Parsed JSON:", data)  # Debugging line
        features = np.array(data['features']).reshape(1, -1)  # Convert input to 2D array
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
