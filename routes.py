from flask import request, jsonify
from main import db, app, ma
from datetime import datetime


class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime, nullable=False)

    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    @property
    def serialize(self):
       return {
           'nom': self.nom,
           'prenom': self.prenom,
           'date_naissance': self.date_naissance
        }

class UtilisateursSchema(ma.ModelSchema):
    class Meta:
       model = Utilisateurs

utilisateur_schema = UtilisateursSchema()

class Biens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    pieces = db.Column(db.Integer(), nullable=False)
    caracteristiques_pieces = db.Column(db.String(200), nullable=False)
    proprietaire_id = db.Column(db.Integer,  db.ForeignKey('utilisateurs.id'), nullable=False)

    def __init__(self, nom, description, type, ville, pieces, caracteristiques_pieces, proprietaire_id):
        self.nom = nom
        self.description = description
        self.type = type
        self.ville = ville
        self.pieces = pieces
        self.caracteristiques_pieces = caracteristiques_pieces
        self.proprietaire_id = proprietaire_id

    @property
    def serialize(self):
       return {
           'nom': self.nom,
           'description': self.description,
           'type': self.type,
           'ville': self.ville,
           'pieces': self.pieces,
           'caracteristiques_pieces': self.caracteristiques_pieces,
           'proprietaire_id': self.proprietaire_id,
       }


class BiensSchema(ma.ModelSchema):
    class Meta:
        model = Biens
    proprietaire = ma.HyperlinkRelated("proprietaire_detail")


@app.route("/")
def hello():
    user = Utilisateurs.query.all()
    schema = UtilisateursSchema(many=True)
    response = schema.dump(user).data
    return jsonify(response)

@app.route('/biens/<string:ville>/')
def show_all_by_city(ville):
    biens = Biens.query.filter_by(ville=ville).all()
    if len(biens) == 0:
        response = {'message': "Il n'y a pas de biens dans cette ville", 'status_code':404}
        return jsonify(response)
    schema = BiensSchema(many=True)
    response = schema.dump(biens).data
    return jsonify(response)


@app.route('/biens/update/<int:id>', methods=['PUT'])
def update_biens(id):
    content = request.get_json()
    try:
        bien = Biens.query.filter_by(id=id).first()
        if bien is None:
            response = {'message': "Le bien a modifier n'existe pas", 'status_code':403}
            return jsonify(response)
        bien.description = content['description']
        bien.nom = content['nom']
        bien.pieces = content['pieces']
        bien.proprietaire_id = content['proprietaire_id']
        bien.type = content['type']
        bien.ville = content['ville']
        bien.caracteristiques_pieces = content['caracteristiques_pieces']
        db.session.commit()
        biens=Biens.query.filter_by(id=id).all()
        schema = BiensSchema()
        response = schema.dump(bien).data
        return jsonify(response)
    except:
        response = {'message': 'Il faut entrer le nom, la description, le nombre de piece et leurs caracteristiques, la proprietaire, le type et la ville du biens a modifier', 'status_code': '400'}
        return jsonify(response)


@app.route('/utilisateurs/update/<int:id>', methods=['PUT'])
def update_utilisateur(id):
    content = request.get_json()
    try:
        utilisateur = Utilisateurs.query.filter_by(id=id).first()
        if utilisateur is None:
            response = {'message': "L'utilisateur a modifier n'existe pas", 'status_code':403}
            return jsonify(response)

        utilisateur.nom = content['nom']
        utilisateur.prenom = content['prenom']
        annee = content['annee']
        mois = content['mois']
        jour = content['jour']
        utilisateur.date_naissance = datetime(annee, mois, jour, 0, 0, 0, 0)
        db.session.commit()
        utilisateur=Utilisateurs.query.filter_by(id=id).all()
        schema = UtilisateursSchema(many=True)
        response = schema.dump(utilisateur).data
        return jsonify(response)
    except:
        response = {'message': 'Il faut entrer le nom, le prenom et la date de naissance de l utilisateur a modifier', 'status_code': '400'}
        return jsonify(response)

@app.route('/utilisateurs/new', methods=['POST'])
def add_utilisateur():
    content = request.get_json()
    try:
        nom = content['nom']
        prenom = content['prenom']
        annee = content['annee']
        mois = content['mois']
        jour = content['jour']
        utilisateur = Utilisateurs.query.filter_by(nom=nom, prenom=prenom).first()
        if utilisateur is None:
            db.session.add(Utilisateurs(nom, prenom, datetime(annee, mois, jour, 0, 0, 0, 0)))
            db.session.commit()
            utilisateur = Utilisateurs.query.filter(Utilisateurs.nom==nom, Utilisateurs.prenom==prenom).all()
            schema = UtilisateursSchema(many=True)
            response = schema.dump(utilisateur).data
            return jsonify(response)
        else:
            response = {'message': 'Cet utilisateur a deja ete cree'}
            return jsonify(response)
    except:
        response = {'message': 'Il faut entrer le nom, le prenom et la date de naissance de l utilisateur a modifier', 'status_code': '400'}
        return jsonify(response)
