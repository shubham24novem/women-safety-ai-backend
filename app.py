from flask import Flask
from flask_cors import CORS
from models.db_models import db
from routes.auth import auth_bp
from routes.contacts import contacts_bp
from routes.sos import sos_bp
from routes.location import location_bp
from routes.voice import voice_bp
from routes.crime import crime_bp
from routes.web import web_bp

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register routes AFTER app is created
app.register_blueprint(auth_bp)
app.register_blueprint(contacts_bp)
app.register_blueprint(sos_bp)
app.register_blueprint(location_bp)
app.register_blueprint(voice_bp)
app.register_blueprint(crime_bp)
app.register_blueprint(web_bp)

@app.route('/')
def home():
    return "Women Safety AI Backend Running"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
app.run(host='0.0.0.0', port=5000, debug=True)