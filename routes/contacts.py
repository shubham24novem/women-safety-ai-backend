from flask import Blueprint, request, jsonify
from models.db_models import db, EmergencyContact

contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/add_contact', methods=['POST'])
def add_contact():
    data = request.json

    contact = EmergencyContact(
        user_id=data['user_id'],
        contact_name=data['contact_name'],
        contact_phone=data['contact_phone']
    )

    db.session.add(contact)
    db.session.commit()

    return jsonify({"message": "Emergency contact added"})


@contacts_bp.route('/get_contacts/<int:user_id>', methods=['GET'])
def get_contacts(user_id):
    contacts = EmergencyContact.query.filter_by(user_id=user_id).all()

    result = []
    for c in contacts:
        result.append({
            "id": c.id,
            "name": c.contact_name,
            "phone": c.contact_phone
        })

    return jsonify(result)