from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/order/<order_id>')
def get_order(order_id):
    return jsonify({"id": order_id, "total": 99.99}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))