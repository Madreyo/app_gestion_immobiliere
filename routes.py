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

    @property
    def serialize(self):
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
    date_naissance = db.Column(db.DateTime)

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/biens/<string:ville>/')
def show_all_by_city(ville):
    biens=Biens.query.filter_by(ville=ville).all()
    return jsonify(Biens=[i.serialize for i in biens])


@app.route('/biens/update/<int:id>', methods=['PUT'])
def update_biens(id):
    bien = Biens.query.filter_by(id=id).first()
    content = request.get_json()
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


@app.route('/utilisateurs/update/<int:id>', methods=['PUT'])
def update_utilisateur(id):
    utilisateur = Utilisateurs.query.filter_by(id=id).first()
    content = request.get_json()
    utilisateur.nom = content['nom']
    utilisateur.prenom = content['prenom']
    utilisateur.date_naissance = content['date_naissance']
    db.session.commit()
    utilisateur=Utilisateurs.query.filter_by(id=id).all()
    return jsonify(Utilisateurs=[i.serialize for i in utilisateur])
