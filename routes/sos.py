from flask import Blueprint, request, jsonify
from utils.sms import send_sos_sms

sos_bp = Blueprint('sos', __name__)

@sos_bp.route('/sos', methods=['POST'])
def sos_alert():
    data = request.json

    name = data.get('name')
    phone = data.get('phone')
    location = data.get('location')

    msg = f"""
🚨 WOMEN SAFETY ALERT!

Name: {name}
Phone: {phone}

Live Location:
{location}
"""

    send_sos_sms("", msg)

    return jsonify({
        "message": "SOS alert sent with GPS"
    })