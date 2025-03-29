from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from config import get_db_connection

app = Flask(__name__)
CORS(app)

# User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                   (data['username'], data['password'], data['role']))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "User registered successfully!"})

# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                   (data['username'], data['password']))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    
    if user:
        return jsonify({"message": "Login successful!", "role": user[2]})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Fetch Features
@app.route('/features', methods=['GET'])
def get_features():
    return jsonify({
        "features": [
            "AI-Powered Learning",
            "Voice Assistance",
            "Personalized Progress Tracking"
        ]
    })

# Fetch Support Information
@app.route('/support', methods=['GET'])
def get_support():
    return jsonify({"support_email": "support@learning.com", "phone": "+123456789"})

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return "Welcome to the AI Job Finder API!"
