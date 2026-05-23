from flask import Blueprint, request, jsonify
from utils.sms import send_sos_sms

sos_bp = Blueprint('sos', __name__)

@sos_bp.route('/sos', methods=['POST'])
def sos_alert():
    data = request.json

    name = data.get('name')
    phone = data.get('phone')
    location = data.get('location')

    contacts = [
        data.get('emergency_contact1'),
        data.get('emergency_contact2'),
        data.get('emergency_contact3'),
        data.get('emergency_contact4'),
    ]

    msg = f"""
🚨 WOMEN SAFETY ALERT!

Name: {name}
Phone: {phone}

Live Location:
{location}
"""

    for contact in contacts:
        if contact:
            send_sos_sms(contact, msg)

    return jsonify({
        "message": "SOS alerts sent successfully"
    })