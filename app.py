from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "DevPipe API is running!",
        "status": "healthy"
    })
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "version": "1.0.0",
        "project": "DevPipe",
        "developer": "Avula Jeevan Yadav"
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)