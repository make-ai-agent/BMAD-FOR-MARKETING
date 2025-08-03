# scripts/prediction_api.py
from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime
import logging

app = Flask(__name__)

# Set up logging for monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variable to store the model
model = None

def load_model():
    """Load the trained predictive model."""
    global model
    try:
        model = joblib.load('conversion_model.joblib')
        logger.info("Model loaded successfully")
        return True
    except FileNotFoundError:
        logger.error("Model file not found. Please train a model first.")
        return False

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "model_loaded": model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """
    Main prediction endpoint.
    Expects JSON: {"spend": float, "ctr": float}
    Returns: {"prediction": int, "probability": float, "timestamp": str}
    """
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'spend' not in data or 'ctr' not in data:
            return jsonify({"error": "Missing required fields: spend, ctr"}), 400
        
        spend = float(data['spend'])
        ctr = float(data['ctr'])
        
        # Make prediction
        features = np.array([[spend, ctr]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0].max()
        
        # Log the prediction for monitoring
        logger.info(f"Prediction made: spend={spend}, ctr={ctr}, prediction={prediction}")
        
        return jsonify({
            "prediction": int(prediction),
            "probability": float(probability),
            "timestamp": datetime.now().isoformat(),
            "input": {"spend": spend, "ctr": ctr}
        })
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({"error": "Prediction failed"}), 500

@app.route('/model/info', methods=['GET'])
def model_info():
    """Get information about the loaded model."""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    return jsonify({
        "model_type": str(type(model).__name__),
        "features": ["spend", "ctr"],
        "target": "conversion_probability",
        "loaded_at": datetime.now().isoformat()
    })

@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """
    Batch prediction endpoint for multiple inputs.
    Expects JSON: {"data": [{"spend": float, "ctr": float}, ...]}
    """
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        data = request.get_json()
        
        if not data or 'data' not in data:
            return jsonify({"error": "Missing 'data' field"}), 400
        
        batch_data = data['data']
        predictions = []
        
        for item in batch_data:
            spend = float(item['spend'])
            ctr = float(item['ctr'])
            features = np.array([[spend, ctr]])
            
            prediction = model.predict(features)[0]
            probability = model.predict_proba(features)[0].max()
            
            predictions.append({
                "prediction": int(prediction),
                "probability": float(probability),
                "input": {"spend": spend, "ctr": ctr}
            })
        
        logger.info(f"Batch prediction completed: {len(predictions)} predictions")
        
        return jsonify({
            "predictions": predictions,
            "count": len(predictions),
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        logger.error(f"Batch prediction error: {str(e)}")
        return jsonify({"error": "Batch prediction failed"}), 500

def main():
    """Main function to run the prediction API."""
    print("--- Starting Predictive Analytics API ---")
    
    # Load the model
    if not load_model():
        print("Failed to load model. Exiting.")
        return
    
    print("Model loaded successfully.")
    print("API endpoints available:")
    print("  GET  /health - Health check")
    print("  GET  /model/info - Model information")
    print("  POST /predict - Single prediction")
    print("  POST /predict/batch - Batch predictions")
    print()
    print("Starting Flask server...")
    
    # In production, use a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    main() 