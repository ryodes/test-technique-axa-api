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

@app.route('/api/devis', methods=['GET'])
def get_devis():
    devis_liste = Devis.query.all()
    result = []

    for devis in devis_liste:
        result.append({
            "id": devis.id,
            "type_ouvrage": devis.type_ouvrage,
            "nom_client": devis.nom_client,
            "numero_opportunite": devis.numero_opportunite,
            "garantie": devis.garantie,
            "destination_ouvrage": devis.destination_ouvrage,
            "type_travaux": devis.type_travaux,
            "cout_ouvrage": devis.cout_ouvrage,
            "presence_existant": devis.presence_existant,
            "client_vip": devis.client_vip,
            "rcmo": devis.rcmo,
            "tarif_trc": devis.tarif_trc,
            "tarif_do": devis.tarif_do,
            "adresse_chantier": devis.adresse_chantier,
            "description": devis.description,
        })

    return jsonify(result)

@app.route("/api/devis", methods=["POST"])
def create_devis():
    data = request.json
    nouveau_devis = Devis(
        type_ouvrage=data.get('typeOuvrage'),
        nom_client=data.get('nomClient'),
        numero_opportunite=data.get('numeroOpportunite'),
        garantie=data.get('garantie'),
        destination_ouvrage=data.get('destinationOuvrage'),
        type_travaux=data.get('typeTravaux'),
        cout_ouvrage=data.get('coutOuvrage'),
        presence_existant=data.get('existant') == 'oui',
        client_vip=data.get('vip') == 'oui',
        rcmo=data.get('rcmo') == 'oui',
        tarif_trc=data.get('tarifTRC'),
        tarif_do=data.get('tarifDO'),
        adresse_chantier=data.get('adresseChantier'),
        description=data.get('description')
    )

    db.session.add(nouveau_devis)
    db.session.commit()

    return jsonify({"message": "Devis reçu", "data": data}), 200

if __name__ == "__main__":
    app.run(debug=True)

# with app.app_context():
#     db.create_all()
