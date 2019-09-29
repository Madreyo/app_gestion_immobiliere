from datetime import datetime, date
from flask import request, flash, url_for, redirect, \
     render_template, jsonify


from main import db, app



class Biens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    ville = db.Column(db.String(100), nullable=False)
    pieces = db.Column(db.Integer(), nullable=False)
    caracteristiques_pieces = db.Column(db.String(200), nullable=False)
    proprietaire = db.Column(db.String(100), nullable=False)

    def __init__(self, nom, description, type, ville, pieces, caracteristiques_pieces, proprietaire):
        self.nom = nom
        self.description = description
        self.type = type
        self.ville = ville
        self.pieces = pieces
        self.caracteristiques_pieces = caracteristiques_pieces
        self.proprietaire = proprietaire

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'nom': self.nom,
           'description': self.description,
           'type': self.type,
           'ville': self.ville,
           'pieces': self.pieces,
           'caracteristiques_pieces': self.caracteristiques_pieces,
           'proprietaire': self.proprietaire,

       }

class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.String(50))

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


@app.route('/biens/<string:ville>')
def show_all_by_city(ville):
    biens=Biens.query.filter_by(ville=ville).all()

    return jsonify(Biens=[i.serialize for i in biens])



@app.route('/biens/update/<int:id>', methods=['PUT'])
def update_biens(id):
    bien = Biens.query.filter_by(id=id).first()
    content = request.get_json()
    try:
        bien.description = content['description']
        bien.nom = content['nom']
        bien.pieces = content['pieces']
        bien.proprietaire = content['proprietaire']
        bien.type = content['type']
        bien.ville = content['ville']
        bien.caracteristiques_pieces = content['caracteristiques_pieces']
        db.session.commit()
        biens=Biens.query.filter_by(id=id).all()
        return jsonify(Biens=[i.serialize for i in biens])
    except:
        return "Il faut entrer le nom, la description, le nombre de piece et leurs caracteristiques, la proprietaire, le type et la ville du biens a modifier"


@app.route('/utilisateurs/update/<int:id>', methods=['PUT'])
def update_utilisateur(id):
    utilisateur = Utilisateurs.query.filter_by(id=id).first()
    content = request.get_json()
    try:
        utilisateur.nom = content['nom']
        utilisateur.prenom = content['prenom']
        utilisateur.date_naissance = content['date_naissance']
        db.session.commit()
        utilisateur = Utilisateurs.query.filter_by(id=id).all()
        return jsonify(Utilisateurs=[i.serialize for i in utilisateur])
    except:
        return "Il faut entrer le nom, le prenom et la date de naissance de l'utilisateur a modifier"

@app.route('/utilisateurs/new', methods=['POST'])
def add_utilisateur():
    content = request.get_json()
    try:
        nom = content['nom']
        prenom = content['prenom']
        date_naissance = content['date_naissance']
        db.session.add(Utilisateurs(nom, prenom, date_naissance))
        db.session.commit()
        utilisateur = Utilisateurs.query.filter(Utilisateurs.nom==nom, Utilisateurs.prenom==prenom, Utilisateurs.date_naissance==date_naissance).all()
        return jsonify(Utilisateurs=[i.serialize for i in utilisateur])
    except:
        return "Il faut entrer le nom, le prenom et la date de naissance de l'utilisateur a creer"
