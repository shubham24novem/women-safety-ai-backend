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
        phone=data['phone']
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
        "phone": user.phone
    })