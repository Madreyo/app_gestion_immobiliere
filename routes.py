from datetime import datetime

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

class Utilisateurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    date_naissance = db.Column(db.DateTime)

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

@app.route("/")
def hello():
    return "Hello World!"
