from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "platform": "secure-kind-cluster"}), 200

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Secure Enterprise Container Platform!"}), 200

if __name__ == '__main__':
    # Running on port 8080
    app.run(host='0.0.0.0', port=8080)