from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 

@app.route("/")
def home():
    return "API Flask en place !"

@app.route("/api/devis", methods=["POST"])
def create_devis():
    data = request.json
    print(data)
    return jsonify({"message": "Devis reçu", "data": data}), 200

if __name__ == "__main__":
    app.run(debug=True)
