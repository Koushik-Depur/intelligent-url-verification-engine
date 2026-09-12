from flask import Flask, request, jsonify
from flask_cors import CORS

import joblib
import pandas as pd

from feature_extraction import extract_features


app = Flask(__name__)

# Allow frontend to communicate with Flask
CORS(app)


# Load trained ML model
model = joblib.load("backend/phishing_model.pkl")


@app.route("/")
def home():

    return jsonify({
        "message": "IVE API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get JSON data from frontend
        data = request.get_json()

        url = data.get("url", "").strip()

        # Check whether URL was provided
        if not url:

            return jsonify({
                "error": "URL is required"
            }), 400


        # Extract URL features
        features = extract_features(url)


        # Convert features into DataFrame
        feature_values = pd.DataFrame(
            [list(features.values())]
        )


        # Make prediction
        prediction = model.predict(feature_values)[0]


        # Get probability
        probabilities = model.predict_proba(
            feature_values
        )[0]


        # Phishing probability
        phishing_probability = probabilities[1]


        # Convert to percentage
        risk_score = round(
            phishing_probability * 100,
            2
        )


        # Determine result
        if prediction == 1:

            result = "Potential Phishing"

        else:

            result = "Predicted Legitimate"


        return jsonify({

            "url": url,

            "prediction": result,

            "risk_score": risk_score,

            "features": features

        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )