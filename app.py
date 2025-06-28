from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Config de la base SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Devis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_ouvrage = db.Column(db.String(50))
    nom_client = db.Column(db.String(100))
    numero_opportunite = db.Column(db.String(50))
    garantie = db.Column(db.String(50))
    destination_ouvrage = db.Column(db.String(100))
    type_travaux = db.Column(db.String(50))
    cout_ouvrage = db.Column(db.Float)
    presence_existant = db.Column(db.Boolean)
    client_vip = db.Column(db.Boolean)
    rcmo = db.Column(db.Boolean)
    tarif_trc = db.Column(db.Float)
    tarif_do = db.Column(db.Float)
    adresse_chantier = db.Column(db.String(255))
    description = db.Column(db.Text)

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

# with app.app_context():
#     db.create_all()
