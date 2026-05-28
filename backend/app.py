from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
CORS(app)

REQUEST_COUNT = Counter('app_requests_total', 'Total App Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        'message': 'Backend API Running Successfully'
    })

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
