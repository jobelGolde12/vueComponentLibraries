from flask import Blueprint, request, jsonify
from DatabaseConnector import db_conn
from database.UserTable import UserAccount

ToLoginLogout = Blueprint('ToLoginLogout', __name__)

@ToLoginLogout.route('/to_login', methods=['POST'])
def toLogin():
    data = request.get_json()
    email = data.get('user_email')
    password = data.get('user_password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    connector = db_conn()
    if not connector:
        return jsonify({"message": "Database connection failed"}), 500

    try:
        user = connector.query(UserAccount).filter_by(email=email).first()

        if user and user.password == password:
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
