# EBG Backend API v2.0 - Full Auth + Notes System
from flask import Flask, jsonify, request
from flask_cors import CORS
from db import table
import psycopg2.extras
import os

app = Flask(__name__)
CORS(app)  # Allow frontend on Vercel to talk to backend on Render

# ─── Create notes table if it doesn't exist ───
def init_db():
    cur = table.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_by VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    table.commit()
    cur.close()

init_db()

# ─── Route: Health Check ───
@app.route('/')
def index():
    return jsonify({"message": "EBG Backend API v2.0 is running!"})

# ─── Route: Sign Up ───
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')

    cur = table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # Check if username already exists
    cur.execute('SELECT * FROM "EBG" WHERE username = %s', (username,))
    if cur.fetchone():
        cur.close()
        return jsonify({"error": "Username already exists"}), 400

    # Insert new user with role 'user'
    cur.execute(
        'INSERT INTO "EBG" (name, username, password, role) VALUES (%s, %s, %s, %s)',
        (name, username, password, 'user')
    )
    table.commit()
    cur.close()
    return jsonify({"message": "Signup successful!"}), 201

# ─── Route: Login ───
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    cur = table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT * FROM "EBG" WHERE username = %s AND password = %s', (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify({
            "message": "Login successful!",
            "user": {
                "id": user['id'],
                "name": user['name'],
                "username": user['username'],
                "role": user['role']
            }
        })
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# ─── Route: Get All Notes (Anyone logged in) ───
@app.route('/notes', methods=['GET'])
def get_notes():
    cur = table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT * FROM notes ORDER BY created_at DESC')
    notes = cur.fetchall()
    cur.close()
    return jsonify(notes)

# ─── Route: Add Note (Admin Only) ───
@app.route('/notes', methods=['POST'])
def add_note():
    data = request.json
    content = data.get('content')
    username = data.get('username')
    role = data.get('role')

    if role != 'admin':
        return jsonify({"error": "Only admins can add notes"}), 403

    cur = table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(
        'INSERT INTO notes (content, created_by) VALUES (%s, %s)',
        (content, username)
    )
    table.commit()
    cur.close()
    return jsonify({"message": "Note added successfully!"}), 201

# ─── Route: Get All Users (Admin Only) ───
@app.route('/users', methods=['GET'])
def get_users():
    cur = table.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT id, name, username, role FROM "EBG"')
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
