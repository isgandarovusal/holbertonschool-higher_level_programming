from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Təhlükəsizlik üçün Secret Key (İstənilən uzun mətn ola bilər)
app.config['JWT_SECRET_KEY'] = 'super-secret-key-123'
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# İstifadəçi bazası (Yaddaşda)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Hissəsi ---

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# --- JWT Authentication Hissəsi ---

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username]['password'], password):
        # Rolu tokenin içinə əlavə edirik (identity olaraq username göndəririk)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# --- Role-based Access Control (RBAC) ---

@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    user_info = users.get(current_user)
    
    if user_info and user_info['role'] == 'admin':
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

# --- JWT Xəta Tənzimləyiciləri (Hamısı 401 qaytarmalıdır) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
