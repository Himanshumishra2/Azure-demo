from flask import Flask, jsonify, request
import requests
import os

USER_SVC = os.getenv('USER_SVC', 'http://user-svc')
ORDER_SVC = os.getenv('ORDER_SVC', 'http://order-svc')

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/')
def index():
    return jsonify({"message": "Gateway - use /user/<id> or /order/<id>"}), 200

@app.route('/proxy/user/<user_id>')
def proxy_user(user_id):
    r = requests.get(f'http://user-svc/user/{user_id}')
    return (r.content, r.status_code, r.headers.items())

@app.route('/proxy/order/<order_id>')
def proxy_order(order_id):
    r = requests.get(f'http://order-svc/order/{order_id}')
    return (r.content, r.status_code, r.headers.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))