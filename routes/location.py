from flask import Blueprint, request, jsonify

location_bp = Blueprint('location', __name__)

@location_bp.route('/location', methods=['POST'])
def update_location():
    data = request.json

    latitude = data['latitude']
    longitude = data['longitude']

    return jsonify({
        "message": "Location received",
        "latitude": latitude,
        "longitude": longitude
    })