from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle Cross-Origin Resource Sharing
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  

model = joblib.load("final_model_cat.pk1")
col_names = joblib.load("col_names_cat.pk1")
scaler = joblib.load("final_scaler_cat.pk1")

# Home route
@app.route("/")
def index():
    return "<h1>Welcome to the Alzheimer's Detection API</h1>"

@app.route('/alzheimers_dectection', methods=['POST'])
def predict():
    try:
        # Check if the request content type is JSON
        if not request.is_json:
            return jsonify({'error': 'Request content type must be application/json'}), 400

        # Parse the JSON input
        feat_data = request.get_json()

        # Validate input format (should be a list of JSON objects)
        if not isinstance(feat_data, list):
            raise ValueError("Input data must be a list of JSON objects.")

        df = pd.DataFrame(feat_data)
        
        df = df.reindex(columns=col_names, fill_value=0)

        # Scale features
        df_scaled = scaler.transform(df)

        # Make predictions
        predictions = model.predict(df_scaled)

        # Prepare response messages
        prediction_messages = [
            '(1) -> Positive Alzheimer diagnosis likely' if pred == 1 
            else '(0) -> Negative Alzheimer diagnosis likely' for pred in predictions
        ]

        # Return predictions
        return jsonify({'prediction': prediction_messages})

    except Exception as e:
        # Catch and return errors
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
