from flask import Blueprint, request, jsonify
from utils.sms import send_sos_sms

voice_bp = Blueprint('voice', __name__)

DISTRESS_WORDS = [
    "help",
    "save me",
    "bachao",
    "emergency",
    "danger"
]

@voice_bp.route('/voice_detect', methods=['POST'])
def voice_detect():
    data = request.json
    text = data.get('text', '').lower()

    for word in DISTRESS_WORDS:
        if word in text:
            msg = f"🚨 WOMEN SAFETY ALERT!\nDistress detected: {text}"
            send_sos_sms("", msg)

            return jsonify({
                "distress": True,
                "detected_text": text,
                "alert_sent": True
            })

    return jsonify({
        "distress": False,
        "detected_text": text,
        "alert_sent": False
    })