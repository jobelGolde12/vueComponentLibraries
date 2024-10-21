from flask import Blueprint, request, jsonify
from DatabaseConnector import db_conn
from database.UserTable import UserAccount

ToCreateDeleteAccount = Blueprint('ToCreateDeleteAccount', __name__)

@ToCreateDeleteAccount.route('/to_create_account', methods=['POST'])
def toCreateAccount():
    data = request.get_json()
    userEmail = data.get('user_email')
    userPassword = data.get('user_password')

    if not userEmail or not userPassword:
        return jsonify({"message": "Email and password are required"}), 400

    connector = db_conn()
    if not connector:
        return jsonify({"message": "Database connection failed"}), 500

    email_exist = connector.query(UserAccount).filter_by(email=userEmail).first()

    if email_exist:
        return jsonify({"message": "Email already exists"}), 409
    
    new_user = UserAccount(email=userEmail, password=userPassword)
    connector.add(new_user)

    try:
        connector.commit()
        return jsonify({"message": "Account created successfully"}), 201
    except Exception as e:
        connector.rollback()
        return jsonify({"error": str(e)}), 500

