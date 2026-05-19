from flask import Blueprint, request, jsonify
from utils.crime_predict import predict_crime

crime_bp = Blueprint('crime', __name__)

@crime_bp.route('/predict_crime', methods=['POST'])
def predict():
    data = request.json

    latitude = data['latitude']
    longitude = data['longitude']
    hour = data['hour']
    crime_count = data['crime_count']

    result = predict_crime(latitude, longitude, hour, crime_count)

    return jsonify({
        "prediction": result
    })