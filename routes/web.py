from flask import Blueprint, render_template

web_bp = Blueprint('web', __name__)

@web_bp.route('/crime_check')
def crime_check():
    return render_template('crime_check.html')