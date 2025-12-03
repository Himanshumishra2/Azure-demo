from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/user/<user_id>')
def get_user(user_id):
    # dummy response
    return jsonify({"id": user_id, "name": "User " + str(user_id)}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))