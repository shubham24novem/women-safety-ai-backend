from flask import Blueprint, request, jsonify
from models.db_models import db, User

auth_bp = Blueprint('auth', __name__)

# REGISTER
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json

    existing_user = User.query.filter_by(email=data['email']).first()

    if existing_user:
        return jsonify({
            "message": "Email already registered"
        }), 400

    user = User(
        full_name=data['full_name'],
        email=data['email'],
        password=data['password'],
        phone=data['phone'],
        emergency_contact1=data['emergency_contact1'],
        emergency_contact2=data['emergency_contact2'],
        emergency_contact3=data['emergency_contact3'],
        emergency_contact4=data['emergency_contact4']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    })


# LOGIN
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(
        email=data['email'],
        password=data['password']
    ).first()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user.id,
        "name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "emergency_contact1": user.emergency_contact1,
        "emergency_contact2": user.emergency_contact2,
        "emergency_contact3": user.emergency_contact3,
        "emergency_contact4": user.emergency_contact4
    })
# UPDATE PROFILE
@auth_bp.route('/update_profile', methods=['POST'])
def update_profile():
    data = request.json

    user = User.query.get(data['user_id'])

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    user.full_name = data['full_name']
    user.phone = data['phone']
    user.emergency_contact1 = data['emergency_contact1']
    user.emergency_contact2 = data['emergency_contact2']
    user.emergency_contact3 = data['emergency_contact3']
    user.emergency_contact4 = data['emergency_contact4']

    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully"
    })
